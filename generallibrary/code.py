

from generallibrary.diagram import TreeDiagram

import pyperclip
import os
import inspect


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


def warn(msg, add_depth=0, print_out=True):
    link = print_link(print_out=False, add_depth=1 + add_depth)
    full_msg = f"Warning: {msg}\n    {link}"
    if print_out:
        print(full_msg)
    return link































