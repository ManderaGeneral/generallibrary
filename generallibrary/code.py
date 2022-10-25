

from generallibrary.diagram import TreeDiagram
from generallibrary.functions import Recycle
from generallibrary.iterables import join_with_str

import pyperclip
import os
import sys
import inspect
import logging

from pathlib import Path


def _name_from_frames():
    return sys._getframe(7).f_globals["__name__"]


class Log(TreeDiagram, Recycle):
    ROOT_NAME = "root"
    FILE_FORMAT = {
        "Level": "%(levelname)-s",
        "Module": "%(name)-s",
        "Time": "%(asctime)-s",
        "MS": "%(msecs)-d",
        "Function": "%(funcName)-s",
        "Line": "%(lineno)d",
        "Message": "%(message)s",
    }
    STREAM_FORMAT = FILE_FORMAT.copy()
    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


    @classmethod
    def _name(cls, name):
        """ Mimic logging.Logger's naming behaviour """
        return str(name) if name else _name_from_frames()

    _recycle_keys = {"name": lambda x: Log._name(x)}

    def __init__(self, name=None, parent=None):
        """ Todo: Make Log use __name__ from previous frame so it doesn't write to root. """
        name = self._name(name)
        self.name = name
        self.logger = logging.getLogger(name)
        assert name == self.logger.name


    def debug(self, *msg):      self.logger.debug(join_with_str(" ", msg))
    def info(self, *msg):       self.logger.info(join_with_str(" ", msg))
    def warning(self, *msg):    self.logger.warning(join_with_str(" ", msg))
    def error(self, *msg):      self.logger.error(join_with_str(" ", msg))
    def critical(self, *msg):   self.logger.critical(join_with_str(" ", msg))
    
    def _configure_helper(self, level, delimiter, format_, handler):
        self.logger.setLevel(level=level)
        formatter = logging.Formatter(fmt=delimiter.join(format_.values()), datefmt=self.DATE_FORMAT)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    
    def _file_handler(self):
        path = Path(f"{self.name}.log.csv")
        file_handler = logging.FileHandler(path)
        if not path.exists() or not path.stat().st_size:
            path.write_text(f'{",".join(self.FILE_FORMAT.keys())}\n')
        return file_handler
    
    def configure_file(self, level=10):
        """ Todo: Use another delimiter than , in Log and make sure it can handle quotes. """
        self._configure_helper(level=level, delimiter=",", format_=self.FILE_FORMAT, handler=self._file_handler())
    
    def configure_stream(self, level=10):
        self._configure_helper(level=level, delimiter=" : ", format_=self.STREAM_FORMAT,
                               handler=logging.StreamHandler())

    @staticmethod
    def loggers():
        return logging.root.manager.loggerDict

    def is_root(self):
        return self.name == self.ROOT_NAME

    def _logger_is_child(self, name: str):
        if self.is_root():
            return "." not in name
        return name.startswith(self.name) and (name.count(".") - self.name.count(".")) == 1

    def _get_parent_name(self):
        if self.is_root():
            return None
        elif "." not in self.name:
            return self.ROOT_NAME
        else:
            return ".".join(self.name.split(".")[0:-1])

    # def spawn_all(self):  # Idea here was to spawn all Logs with a sorted list of logger names which is faster
    #     sorted(self.loggers().keys())

    def spawn_parents(self):
        if not self.is_root():
            parent_log = type(self)(name=self._get_parent_name())
            self.set_parent(parent=parent_log)

    def spawn_children(self):
        for name, logger in self.loggers().items():
            if self._logger_is_child(name=name):
                type(self)(name=name, parent=self)

    def __repr__(self):
        return f"<Log: '{self.name}'>"


def clipboard_copy(s):
    """ Copy a string to clipboard.
        Rudely tries to installs xclip on linux if it fails. """
    def _call():
        return pyperclip.copy(s)

    try:
        _call()
    except pyperclip.PyperclipException:
        os.system("sudo apt-get install xclip")
        _call()


def clipboard_get():
    """ Get clipboard string. """
    return pyperclip.paste()


class CodeLine(TreeDiagram):
    """ Tool to help with printing code line by line.
        Top parent is ignored when printing. """
    indent_str = " " * 4

    def __init__(self, code_str=None, space_before=0, space_after=0, parent=None):
        if code_str is None:
            code_str = ""
        self.code_str = code_str
        self.space_before = space_before
        self.space_after = space_after

    def __str__(self):
        return self.text()

    def __contains__(self, item):
        return str(self).__contains__(item)

    def get_lines(self, watermark=True):
        """ Generate a list of formatted code lines by iterating stored _Line instances. """
        lines = []
        for codeLine in self.get_all():
            lines.extend([""] * codeLine.space_before)
            if codeLine.code_str:
                lines.append(f"{self.indent_str * (len(codeLine.get_parents(depth=-1)) - 1)}{codeLine.code_str}")
            lines.extend([""] * codeLine.space_after)

        if watermark:
            lines.insert(0, "# -------------------- GENERATED CODE --------------------")
            lines.append("# --------------------------------------------------------")

        return lines

    def text(self, watermark=False):
        """ Generate and print copyable code. """
        code = "\n".join(self.get_lines(watermark=watermark))
        return code


def debug(scope, *evals, print_out=True):
    """
    Easily call eval() on an arbitrary amount of evaluation strings.
    Useful for debugging.

    Example:
        debug(locals(), "value", "value + jumpValue", print_out=True)
        debug(locals())  # Prints all objects in scope

    :param dict scope: Just write locals()
    :param str evals: Variable names with or without operations
    :param print_out: Whether to print directly or not
    :return: A nicely formatted string
    """
    if not evals:
        evals = list(scope.keys())

    lines = []
    n = max([len(string) for string in evals])
    for evalStr in evals:
        try:
            result = eval(evalStr, scope)
        except:
            result = "ERROR"
        lines.append(f"{evalStr:>{n}} = {result}")
    lines.append("")
    text = "\n".join(lines)
    if print_out:
        print(text)
    return text


def get_origin(obj, include_depth=False):
    """ Dig up original obj that might be wrapped or a property. """
    depth = 0
    while True:
        if isinstance(obj, property):
            obj = obj.fget
        elif hasattr(obj, "__wrapped__"):
            obj = obj.__wrapped__
        elif hasattr(obj, "__func__"):
            obj = obj.__func__
        else:
            break
        depth += 1

    if include_depth:
        return obj, depth
    else:
        return obj


# https://stackoverflow.com/questions/26300594/print-code-link-into-pycharms-console
def print_link(file=None, line=None, print_out=True, add_depth=0):
    """ Print a link in PyCharm to a line in file.
        Defaults to line where this function was called. """
    level = inspect.stack()[1 + add_depth]
    if file is None:
        file = level.filename
    if line is None:
        line = level.lineno
    string = f'File "{file}", line {max(line, 1)}'.replace("\\", "/")

    if print_out:
        print(string)
    return string


def print_link_to_obj(obj, print_out=True):
    """ Print a link in PyCharm to a module, function, class, method or property. """
    line = get_definition_line(obj=obj)

    obj = get_origin(obj=obj)
    file = inspect.getfile(obj)
    return print_link(file=file, line=line, print_out=print_out)


def get_definition_line(obj):
    """ Get line number of an object's definition. """
    obj, depth = get_origin(obj=obj, include_depth=True)
    return max(inspect.getsourcelines(obj)[1] + depth, 1)































