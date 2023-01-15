from typing import Union

from generallibrary.decorators import wrapper_transfer, SigInfo
from generallibrary.iterables import remove

import re

import json
import subprocess
import sys
from collections import ChainMap

import pandas as pd


class classproperty:
    """ Just like @property but for a class method.
        @classproperty
        def foo(cls):
            return cls.bar
        https://stackoverflow.com/a/13624858/3936044 """
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, owner_self, owner_cls):
        return self.fget(owner_cls)




def _tokenize(expression):
    """ Tokenize an expression.
        Taken from myself at https://stackoverflow.com/questions/61948141/python-function-from-mathematical-expression-string/61949248 """
    return re.findall(r"(\b\w*[.]?\w+\b|[()+*\-/])", expression)


ignore = ["+", "-", "*", "/", "(", ")", "sqrt"]

def calculate(expression, *args):
    """ Automatically fills variables of a formula in a string then evaluates it.
        Enter args in the order that they appear. """
    seenArgs = {}
    newTokens = []
    tokens = _tokenize(expression)
    for token in tokens:
        try:
            float(token)
        except ValueError:
            tokenIsFloat = False
        else:
            tokenIsFloat = True

        if token in ignore or tokenIsFloat:
            newTokens.append(token)
        else:
            if token not in seenArgs:
                seenArgs[token] = str(args[len(seenArgs)])
            newTokens.append(seenArgs[token])
    return eval("".join(newTokens))


def defaults(dictionary, overwriteNone=False, **kwargs):
    """
    Set default values of a given dictionary, option to overwrite None values.
    Returns given dictionary with values updated by kwargs unless they already existed.

    :param dict dictionary:
    :param overwriteNone: Whether to overwrite None values.
    :param kwargs:
    """
    for key, value in dictionary.items():
        dictValueIsNone = value is None
        kwargsHasValue = key in kwargs
        if overwriteNone and dictValueIsNone and kwargsHasValue:
            continue

        # Overwrite kwargs with dictionary
        kwargs[key] = value

    return kwargs


class EmptyContext:
    """ Class for an empty context manager.
        Used for creating a "fake" lock for example in Path. """
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class CallTable:
    """ Create a markdown table of functions and arguments. """
    def __init__(self, name=None):
        self.name = name

        self.funcs = {}
        self.args = {}

    def set_funcs(self, **funcs):
        """ Set all funcs. """
        self.funcs = funcs
        return self

    def set_args(self, **args):
        """ Set all args. """
        self.args = args
        return self

    def _generate(self, funcs=None, args=None, print_out=True):
        if funcs is None:
            funcs = self.funcs
        if args is None:
            args = self.args

        columns = {}
        for func_name, func in funcs.items():
            columns[func_name] = {}
            for arg_name, arg in args.items():
                try:
                    result = func(arg)
                    if not result:
                        result = ""
                except Exception as e:
                    # raise e
                    result = "-"
                columns[func_name][arg_name] = result

        df = pd.DataFrame(columns)
        df = df.rename_axis(self.name)

        md = df.to_markdown()
        if print_out:
            print(md, "\n")
        return md

    def generate(self, print_out=True):
        """ Generate table with stored funcs and args. """
        return self._generate(print_out=print_out)

    def generate_with_args(self, print_out=True, **args):
        """ Generate table with stored funcs and new args. """
        return self._generate(args=args, print_out=print_out)

    def generate_with_funcs(self, print_out=True, **funcs):
        """ Generate table with stored args and new funcs. """
        return self._generate(funcs=funcs, print_out=print_out)


def initBases(cls):
    """
    Decorator function for class to automatically initalize all inherited classes.

    Wrap a class' unbound __init__ method to take any arguments.
    When wrapper is called it iterates DIRECT bases to call their unbound __init__ methods along with it's own original __init__.

    Also looks for defined `__init_post__` methods, stores them in `instance.__init_post__s` and calls them all after all inits.
    """
    cls_init = cls.__init__  # Unbound original __init__ method of class

    if getattr(cls, "_is_wrapped_by_initBases", None) is cls:
        return cls

    cls._is_wrapped_by_initBases = cls

    def _wrapper(*args, **kwargs):
        cls_SigInfo = SigInfo(cls_init, *args, **kwargs)

        if cls_SigInfo["self"] is None:
            print(cls_SigInfo["self"])
            raise AttributeError(f"{cls} hasn't defined it's `__init__`")

        initialized_bases = []



        if not hasattr(cls_SigInfo["self"], "__init_post__s"):
            cls_SigInfo["self"].__init_post__s = []
        post_inits = cls_SigInfo["self"].__init_post__s

        for base in cls.__bases__ + (cls, ):
            init = cls_init if base is cls else base.__init__
            # print(init)

            if init is not object.__init__ and init not in initialized_bases:
                if getattr(cls_SigInfo["self"], "_recycle_is_new", True):
                    cls_SigInfo.call(child_callable=init)
                initialized_bases.append(init)

            if getattr(base, "__init_post__", None) and base.__init_post__ not in post_inits:
                post_inits.append(base.__init_post__)

        if cls is cls_SigInfo["self"].__class__ and getattr(cls_SigInfo["self"], "_recycle_is_new", True):
            for post_init in post_inits:
                cls_SigInfo.call(child_callable=post_init)

    cls.__init__ = wrapper_transfer(cls.__init__, _wrapper)
    return cls


def auto_deco(deco):
    """ Automatically call deco on class and all its subclasses. """
    class AutoDecoMetaClass(type):
        def __init__(cls, *args, **kwargs):
            type.__init__(deco(cls), *args, **kwargs)
    return AutoDecoMetaClass

AutoInitBases = auto_deco(initBases)


class HierarchyStorer:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        setattr(HierarchyStorer, cls.__name__, cls)


class Recycle:
    """ Inherit this class to make instantiating two classes with the same args yield the same instance object.
        Assign _recycle_keys to a dict with keys corresponding to init args and value being a func (str() in most cases) to return json serializable obj.
        _recycle_keys are combined in case of inheritence.
        Set to empty dict for singleton.

        Any parameter values are used if the parameter name matches.
        'cls' is always set to the class being initialized.
        If there's a parameter value missing in _recycle_keys then it looks for a parameter which has the same name as the key in the dict for this func.

        Stores instances in top most cls.
        Puts cls.__name__ in key so inheritence returns actual class called, preventing different class calls to return same instance.
        Note: Does not work with pickle. """
    _recycle_keys = None
    _recycle_is_new = None
    _recycle_instances = None

    _CLS_PAR_NAME = "cls"

    @staticmethod
    def _recycle_deco_init(func):
        def _wrapper(self, *args, **kwargs):
            if self._recycle_is_new:
                func(self, *args, **kwargs)
        return wrapper_transfer(func, _wrapper)

    @classmethod
    def _recycle_key_error(cls):
        from generallibrary.code import print_link_to_obj
        print_link_to_obj(cls)
        raise AttributeError(f"{cls} hasn't configured its '_recycle_keys'.")

    @classmethod
    def assert_max_one_missing_name(cls, siginfo_primary, siginfo_secondary):
        missing_names = set(siginfo_secondary.names) - set(siginfo_primary.names)
        missing_names.discard(cls._CLS_PAR_NAME)
        if len(missing_names) > 1:
            raise AttributeError(f"Cannot miss more than one name '{missing_names}' for recycle key func {siginfo_secondary.callableObject}.")

    @classmethod
    def _get_recycle_keys(cls):
        """ Iterate all bases to extract and combine their _recycle_keys dicts.
            ChainMap will pick left-most if duplicate. """
        all_recycle_keys = get_attrs_from_bases(cls, "_recycle_keys", ignore=None)
        recycle_keys = ChainMap(*all_recycle_keys)
        if not all_recycle_keys:
            cls._recycle_key_error()
        return recycle_keys

    @classmethod
    def _recycle_single_func_in_dict(cls, siginfo, name, func):
        func_siginfo = SigInfo(func)
        func_siginfo[cls._CLS_PAR_NAME] = cls
        cls.assert_max_one_missing_name(siginfo, func_siginfo)
        for name_in_func in func_siginfo.names:
            if name_in_func == cls._CLS_PAR_NAME:
                continue
            elif name_in_func in siginfo.names:
                func_siginfo[name_in_func] = siginfo[name_in_func]
            else:
                if name not in siginfo.names:
                    raise AttributeError(f"Parameter '{name_in_func}' is missing and so was parameter '{name}' which was the key.")
                func_siginfo[name_in_func] = siginfo[name]
        return func_siginfo.call()

    @classmethod
    def _recycle_key(cls, args, kwargs):
        sigInfo = SigInfo(cls.__init__, None, *args, **kwargs)
        recycle_keys = cls._get_recycle_keys()
        recycle_list = []
        for name, func in recycle_keys.items():
            recycle_list.append(cls._recycle_single_func_in_dict(siginfo=sigInfo, name=name, func=func))
        recycle_list.append(cls.__name__)

        try:
            return json.dumps(recycle_list)
        except TypeError as e:
            raise TypeError(f"{recycle_list} isn't serializable") from e

    def __new__(cls, *args, **kwargs):
        key = cls._recycle_key(args, kwargs)

        if cls._recycle_instances is None:
            cls._recycle_instances = {}

        is_new = key not in cls._recycle_instances
        if is_new:
            cls._recycle_instances[key] = object.__new__(cls)
        instance = cls._recycle_instances[key]
        instance._recycle_is_new = is_new
        return instance

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if cls.__init__ is not object.__init__:
            cls.__init__ = cls._recycle_deco_init(cls.__init__)

    def recycle_clear(self):
        """ Remove this stored instance from recyclables. """
        return remove(self._recycle_instances, self)

    @classmethod
    def recycle_clear_all(cls):
        """ Clear all recyclables. """
        if isinstance(cls._recycle_instances, dict):
            cls._recycle_instances.clear()

def _decode_subprocess(byte_string):
    if type(byte_string) is not bytes:
        return byte_string
    return byte_string.decode(sys.stdout.encoding)

def _call(args, kwargs, python, capture_output):
    args = [str(arg) for arg in args]
    if python:
        args.insert(0, sys.executable)

    if capture_output:
        return subprocess.check_output(args=args, stderr=subprocess.STDOUT, **kwargs)
    else:
        return subprocess.check_call(args=args, **kwargs)

_sentinel = object()
def terminal(*args, python=False, error=True, default=_sentinel, capture_output=True, **kwargs):
    try:
        byte_string = _call(args=args, kwargs=kwargs, python=python, capture_output=capture_output)
    except subprocess.CalledProcessError as exception:
        # return exception
        if default is _sentinel:
            if error:
                raise ChildProcessError(_decode_subprocess(byte_string=exception.output))
        else:
            return default
        return _decode_subprocess(byte_string=exception.output)
    return _decode_subprocess(byte_string=byte_string)



class _Result_Terminal:
    success = None
    fail = None
    string_result = None
    code_result = None
    error_result = None

    @staticmethod
    def _decode(byte_string):
        # https://stackoverflow.com/a/24638593/3936044
        if type(byte_string) is not bytes:
            return byte_string
        return byte_string.decode(sys.stdout.encoding)

    def _process_result(self, success=None, error=None):
        """ :param generallibrary.Terminal self: """
        self.success = error is None
        self.fail = not self.success

        if self.success:
            self.string_result = str(success, "utf-8")
        elif self.default is self.SENTINEL:
            self.string_result = str(error.output, "utf-8")
        else:
            self.string_result = self.default

        self.code_result = error.returncode if error else 0
        self.error_result = error


class Terminal(_Result_Terminal):
    """ One-time use terminal call.
        If error and sentinel is defined then string_result will be set to default. Success will still be False. """

    ERROR = subprocess.CalledProcessError
    SENTINEL = object()

    def __init__(self, *args, python=False, error=True, default=SENTINEL, capture_output=True, **kwargs):
        self.args = args
        self.python = python
        self.raise_error = error
        self.default = default
        self.capture_output = capture_output
        self.kwargs = kwargs

        self.call()

    def _call(self):
        if self.capture_output:
            return subprocess.check_output(args=self.get_args(), stderr=subprocess.STDOUT, **self.kwargs)
        else:
            return subprocess.check_call(args=self.get_args(), **self.kwargs)

    def call(self):
        try:
            self._process_result(success=self._call())
        except self.ERROR as exception:
            if self.raise_error and self.default is self.SENTINEL:
                raise
            self._process_result(error=exception)

    def get_args(self):
        args = [str(arg) for arg in self.args]
        if self.python:
            args.insert(0, sys.executable)
        return args



from generallibrary.objinfo.objinfo import get_attrs_from_bases































