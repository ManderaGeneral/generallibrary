import inspect
import re
import functools
import pandas as pd


def deco_cache():
    """ Enable caching for a method or function. """
    return functools.lru_cache()


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


class SigInfo:
    """
    Handles a callable along with it's parameters.
    Forgiving as it sets missing values to None.
    Parameters can be changed but not callableObject.
    Args are unpacked to allArgs using parameters of callableObject.
    If there's a *packedParameter then it's stored as a list inside allArgs.
    TODO: Add caching for SigInfo's signature methods
    """
    def __init__(self, /, callableObject, *args, **kwargs):  # / to end positional only characters, allows us to have "self" in kwargs for unbound methods
        assert callable(callableObject)

        self._callableObject = callableObject
        self.allArgs = {**self.defaults, **self._argsToKwargs(args), **kwargs}

    def _argsToKwargs(self, args):
        kwargs = {}
        for i, (name, arg) in enumerate(zip(self.positionalArgNames, args)):
            if name == self.packedArgsName:
                kwargs[name] = list(args[i:])
                assert i + 1 == len(self.positionalArgNames)  # Make sure this is last iteration becuse *args should be last
            else:
                kwargs[name] = arg
        return kwargs

    @property
    def callableObject(self):
        """ Propertize to protect but still have public. """
        return self._callableObject

    def class_from_callable(self, meth=None):
        """ Return class that owns given method, or given callable from initiating SigInfo.

            https://stackoverflow.com/questions/3589311/get-defining-class-of-unbound-method-ect-in-python-3/25959545#25959545 """
        meth = meth if meth else self.callableObject
        if isinstance(meth, functools.partial):
            return self.class_from_callable(getattr(meth, "func"))
        if inspect.ismethod(meth) or (inspect.isbuiltin(meth) and getattr(meth, '__self__', None) is not None and getattr(meth.__self__, '__class__', None)):
            for cls in inspect.getmro(meth.__self__.__class__):
                if meth.__name__ in cls.__dict__:
                    return cls
            meth = getattr(meth, '__func__', meth)  # fallback to __qualname__ parsing
        if inspect.isfunction(meth):
            cls = getattr(inspect.getmodule(meth),
                          meth.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0],
                          None)
            if isinstance(cls, type):
                return cls
        return getattr(meth, '__objclass__', None)  # handle special descriptor objects

    # ========= Level 1 - SIGNATURE PARAMETERS =========

    @property
    def positional_extra(self):
        """ Get a list of the positional parameter names, including self or cls.
            A bit sketchy. """
        try:
            return inspect.getfullargspec(self.callableObject).args  # Cannot handle @deco_cached
        except TypeError:
            return self.positionalArgNames

    @property
    def parameters(self):
        """ Get list of inspect parameter objects. """
        return list(inspect.signature(self.callableObject).parameters.values())

    @property
    def names(self):
        """ Get list of parameter names. """
        return [param.name for param in self.parameters]

    @property
    def namesWithoutDefaults(self):
        """ Get list of parameter names except those ones that have a default value. """
        return [name for name in self.names if name not in self.defaults]

    @property
    def namesRequired(self):
        """ Get list of parameter that have to be defined, i.e. non-packed without default value. """
        return [name for name in self.names if name not in list(self.defaults.keys()) + [self.packedArgsName, self.packedKwargsName]]

    @property
    def namesWithoutPacked(self):
        """ Get list of parameter names except *args or **kwargs. """
        return [name for name in self.names if name not in (self.packedArgsName, self.packedKwargsName)]

    @property
    def leadingArgNames(self):
        """ Get names leading args that don't have default value.
            '*args' wont be included.
            'self' wont be included. """
        leadingArgNames = []
        for param in self.parameters:
            if param.name == "self":
                continue

            noDefault = param.default is inspect.Parameter.empty
            includedKind = param.kind.name in ("POSITIONAL_OR_KEYWORD", "POSITIONAL_ONLY")
            if not (noDefault and includedKind):
                break

            leadingArgNames.append(param.name)
        return leadingArgNames

    @property
    def packedArgsName(self):
        """ Get name of packed *args or None. """
        for param in self.parameters:
            if param.kind.name == "VAR_POSITIONAL":
                return param.name

    @property
    def packedKwargsName(self):
        """ Get name of packed *kwargs or None. """
        for param in self.parameters:
            if param.kind.name == "VAR_KEYWORD":
                return param.name

    @property
    def defaults(self):
        """ Get dict of default values. """
        d = {param.name: param.default for param in self.parameters if param.default is not param.empty}

        if "self" in self.names and "self" not in d:
            d["self"] = self.callableObject

        return d

    @property
    def positionalOnlyArgNames(self):
        """ Get list of parameter names that can ONLY take a positional argument.
            Note - Can be changed dynamically: If packedArgs isn't None then all `POSITIONAL_OR_KEYWORD` are included. """
        if self.packedArgs:
            return self.positionalArgNames
        else:
            return [param.name for param in self.parameters if param.kind.name in ("POSITIONAL_ONLY", "VAR_POSITIONAL")]

    @property
    def positionalOnlyOppositeArgNames(self):
        """ Get list of parameter names that CAN take a keyword argument.
            Opposite of `self.poisitionalOnlyArgNames`. """
        return [name for name in self.names if name not in self.positionalOnlyArgNames]


    @property
    def positionalArgNames(self):
        """
        Get list of parameter names that CAN take a positional argument.
        `*args` included but is always last if it exists.
        """
        return [param.name for param in self.parameters if param.kind.name in ("POSITIONAL_ONLY", "POSITIONAL_OR_KEYWORD", "VAR_POSITIONAL")]

    @property
    def positionalOppositeArgNames(self):
        """
        Get list of parameter names that can ONLY take a keyword argument.
        Opposite of `self.positionalArgNames`.
        `**kwargs` included but is always last if it exists.
        """
        return [name for name in self.names if name not in self.positionalArgNames]

    def getIndexFromName(self, name):
        """ Get index from name if name exists, else None. """
        if name in self.names:
            return self.names.index(name)

    # ========= Level 2 =========
    @property
    def packedArgs(self):
        """ Return a list of values in packed args parameter, empty list if there are no packed args. """
        return self.allArgs.get(self.packedArgsName, [])

    @property
    def packedKwargs(self):
        """ Return a dict of values in packed kwargs parameter, empty dict if there are no packed kwargs. """
        return {key: value for key, value in self.allArgs.items() if self.packedKwargsName and key not in self.names}

    @property
    def unpackedArgs(self):
        """ Extract a list of all positional ONLY parameters for callable. """
        args = []
        for name in self.positionalOnlyArgNames:
            if name == self.packedArgsName:
                args.extend(self.packedArgs)
            else:
                args.append(self[name])
        return args

    @property
    def unpackedKwargs(self):
        """ Extract a dict of key words that callable can take. """
        if self.packedKwargsName:  # Give everything except possible positional only arguments
            return {key: value for key, value in self.allArgs.items() if key not in self.positionalOnlyArgNames}
        else:  # Return every parameter except positional only
            return {key: self[key] for key in self.positionalOnlyOppositeArgNames}

    # ========= Level 3 =========

    def __getitem__(self, name):
        """ Get value of a parameter from allArgs, otherwise None. """
        return self.allArgs.get(name, self.defaults.get(name, None))

    def __setitem__(self, name, value):
        """ Can set single keyword argument or entire *args."""
        self.allArgs[name] = value

    def call(self, child_callable=None):
        """ Calls own callableObject or given child callable with filled args and kwargs.
            Unfilled required parameters will get a None value. """
        if child_callable:
            return SigInfo(child_callable, **self.allArgs).call()
        else:
            return self.callableObject(*self.unpackedArgs, **self.unpackedKwargs)

    # ========= Other =========

    def __repr__(self):
        return f"<SigInfo for '{self.callableObject.__class__.__name__}' with names '{', '.join(self.names)}'>"


ignore = ["+", "-", "*", "/", "(", ")", "sqrt"]


def _tokenize(expression):
    """
    Tokenize an expression
    Taken from myself at https://stackoverflow.com/questions/61948141/python-function-from-mathematical-expression-string/61949248
    """
    return re.findall(r"(\b\w*[.]?\w+\b|[()+*\-/])", expression)


def calculate(expression, *args):
    """
    Automatically fills variables of a formula in a string then evaluates it.
    Enter args in the order that they appear.
    """
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


class Operators:
    """Automatic operator definitions for classes."""
    comparisons = {
        "__eq__": lambda a, b: a == b,
        "__gt__": lambda a, b: a > b,
        "__lt__": lambda a, b: a < b,
        "__ge__": lambda a, b: a >= b,
        "__le__": lambda a, b: a <= b,
    }

    @classmethod
    def deco_define_comparisons(cls, leftLambda, rightLambda):
        """
        Define all comparision operators for this class.
        Provide two functions that return left and right values.
        Automatically fills 'left' and 'right' parameters by name.
        Will make class instances unhashable as the `__eq__` method is defined without defining `__hash__`.

        Stubs:
            def __eq__(self, other): ...
            def __gt__(self, other): ...
            def __lt__(self, other): ...
            def __ge__(self, other): ...
            def __le__(self, other): ...
        """
        def wrapper(baseCls):
            """."""
            for name, func in cls.comparisons.items():

                lambdaFunc = lambda left, right, func=func: func(
                    SigInfo(leftLambda, left=left, right=right).call(),
                    SigInfo(rightLambda, left=left, right=right).call())
                setattr(baseCls, name, lambdaFunc)

            return baseCls
        return wrapper


def deco_cast_parameters(**pars_to_cast):
    """ Decorator to make sure `path` parameter is a Path.
        Example: @deco_cast_paramters(x=int, y=Vec2) """
    def _decorator(function):
        def _wrapper(*args, **kwargs):
            sigInfo = SigInfo(function, *args, **kwargs)

            for par_name, cls in pars_to_cast.items():
                if par_name not in sigInfo.names:
                    raise AttributeError(f"Function does not have a `{par_name}` parameter.")
                if not typeChecker(sigInfo[par_name], cls, error=False):
                    sigInfo[par_name] = cls(sigInfo[par_name])

            return sigInfo.call()
        return _wrapper
    return _decorator


def deco_default_self_args(func):
    """ As an alternative to setting each and every parameter's default value to `None` for a method.
        Automatically sets each undefined parameter to self's attribute, which allows us to set a parameter `None`.
        Note: Parameters names must match attributes in self. """
    def _wrapper(*args, **kwargs):
        sigInfo = SigInfo(func, *args, **kwargs)

        for required_parameter in sigInfo.namesRequired:
            if required_parameter not in sigInfo.allArgs:
                try:
                    attr_value = getattr(sigInfo["self"], required_parameter)
                except AttributeError:
                    raise AttributeError(f"Missing attribute '{required_parameter}' for instance '{sigInfo['self']}'.")
                sigInfo[required_parameter] = attr_value

        return sigInfo.call()
    return _wrapper


def deco_extend(outer_cls):
    """ Allows additional arguments when inheriting and extending a built-in.
        Overrides __new__ to call cls' first base's __new__ with the single first given argument.
        Todo: Test deco_extend with int and str. """
    def __new__(cls, *args, **kwargs):
        arg = args[0] if args else next(iter(kwargs.values()))
        return cls.__bases__[0].__new__(cls, arg)

    outer_cls.__new__ = __new__
    return outer_cls


class EmptyContext:
    """ Class for an empty context manager. """
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
                # print(arg, getattr(arg, "__self__", None))
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

    def generate(self):
        """ Generate table with stored funcs and args. """
        return self._generate()

    def generate_with_args(self, **args):
        """ Generate table with stored funcs and new args. """
        return self._generate(args=args)

    def generate_with_funcs(self, **funcs):
        """ Generate table with stored args and new funcs. """
        return self._generate(funcs=funcs)


from generallibrary.types_ import typeChecker

































