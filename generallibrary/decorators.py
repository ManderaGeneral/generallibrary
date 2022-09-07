import functools
import inspect

from generallibrary.types import typeChecker, getBaseClassNames

def wrapper_transfer(base, target):
    """ Update a wrappers' metadata with base function's to properly propagate info. """
    for attr in ("__doc__", "__module__", "__name__"):
        if hasattr(base, attr):
            setattr(target, attr, getattr(base, attr))
    setattr(target, "__wrapped__", base)
    return target


def deco_cache():
    """ Enable caching for a method or function.
        Put after possible static/class method deco.
        Can change to functools.cache when 3.8 support is dropped. """
    return functools.lru_cache()


class SigInfo:
    """ Handles a callable along with it's parameters.
        Forgiving as it sets missing values to None.
        Parameters can be changed but not callableObject.
        Args are unpacked to allArgs using parameters of callableObject.
        If there's a *packedParameter then it's stored as a list inside allArgs. """
    def __init__(self, /, callableObject, *args, **kwargs):  # / to end positional only characters, allows us to have "self" in kwargs for unbound methods
        assert callable(callableObject)

        self._args = args
        self._kwargs = kwargs

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
    @deco_cache()
    def parameters(self):
        """ Get list of inspect parameter objects. """
        try:
            return list(inspect.signature(self.callableObject).parameters.values())
        except ValueError:
            return self._custom_signature()

    @deco_cache()
    def _custom_signature(self):
        signature_method = getattr(self, f"_signature_{self.callableObject.__name__}", None)
        if signature_method is None:
            raise ValueError(f"Missing signature for {self.callableObject}")
        return signature_method()

    @staticmethod
    def _signature_int():
        return [
            inspect.Parameter(name="x", kind=inspect.Parameter.POSITIONAL_ONLY, default=0),
            # inspect.Parameter(name="base", kind=inspect.Parameter.POSITIONAL_OR_KEYWORD, default=None),  # Couldn't get base to work
        ]

    @staticmethod
    def _signature_str():
        return [
            inspect.Parameter(name="object", kind=inspect.Parameter.POSITIONAL_OR_KEYWORD, default=""),
        ]

    @staticmethod
    def _signature_bool():
        return [
            inspect.Parameter(name="__o", kind=inspect.Parameter.POSITIONAL_ONLY, default=False),
        ]

    @staticmethod
    def _signature_dict():
        return [
            inspect.Parameter(name="args", kind=inspect.Parameter.VAR_POSITIONAL),
            inspect.Parameter(name="kwargs", kind=inspect.Parameter.VAR_KEYWORD),
        ]

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

    def call(self, child_callable=None, args_first=False):
        """ Calls own callableObject or given child callable with filled args and kwargs.
            Unfilled required parameters will get a None value. """
        if child_callable:
            return SigInfo(child_callable, **self.allArgs).call()
        else:
            return self.callableObject(*self.unpackedArgs, **self.unpackedKwargs)

    # ========= Other =========

    def __repr__(self):
        return f"<SigInfo for '{self.callableObject.__name__}' with names '{', '.join(self.names)}'>"
        # return f"<SigInfo for '{self.callableObject.__class__.__name__}' with names '{', '.join(self.names)}'>"


def deco_optional_suppress(*exceptions, return_bool=True):
    """ Requires an "error" arg for decorated func.
        If error is False and a specified exception is caught then it just returns False if return_bool else None.
        If no exception is raised it returns True if return_bool else func_result. """
    def _deco(func):
        def _wrapper(*args, **kwargs):
            sigInfo = SigInfo(func, *args, **kwargs)
            assert "error" in sigInfo.names

            if sigInfo["error"]:
                result = func(*args, **kwargs)
                return True if return_bool else result
            else:
                try:
                    result = func(*args, **kwargs)
                except exceptions:
                    return False if return_bool else None
            return True if return_bool else result

        return _wrapper
    return _deco


def deco_cast_parameters(**pars_to_cast):
    """ Decorator to make sure `path` parameter is a Path for example.
        Example: @deco_cast_parameters(x=int, y=Vec2) """
    def _decorator(func):
        def _wrapper(*args, **kwargs):
            sigInfo = SigInfo(func, *args, **kwargs)

            for par_name, cls in pars_to_cast.items():
                if par_name not in sigInfo.names:
                    raise AttributeError(f"Function does not have a `{par_name}` parameter.")
                if not typeChecker(sigInfo[par_name], cls, error=False):
                    sigInfo[par_name] = cls(sigInfo[par_name])

            return sigInfo.call()
        return wrapper_transfer(func, _wrapper)
    return _decorator


def deco_cast_to_self(if_not_base):
    """ Cast arg(s) to self's type if if_not_base isn't a base of first arg. """
    def _deco(func):
        def _wrapper(self, *args, **kwargs):
            combined = args + tuple(kwargs.values())
            # is_same_class = type(combined[0]) == type(self)
            # if combined and (combined[0] is None or is_same_class):
            if combined and (combined[0] is None or if_not_base in getBaseClassNames(combined[0], includeSelf=True)):
                arg = combined[0]
            else:
                arg = type(self)(*args, **kwargs)
            return func(self, arg)
        return wrapper_transfer(func, _wrapper)
    return _deco


def deco_bound_defaults(func):
    """ As an alternative to setting each and every parameter's default value to `None` for a method.
        Automatically sets each undefined parameter to self's attribute, which allows us to set a parameter `None`.
        Note: Parameters names must match attributes in self. """
    def _wrapper(*args, **kwargs):
        sigInfo = SigInfo(func, *args, **kwargs)
        obj = sigInfo["self"] if "self" in sigInfo.names else sigInfo["cls"]

        for required_parameter in sigInfo.namesRequired:
            if required_parameter not in sigInfo.allArgs:
                try:
                    attr_value = getattr(obj, required_parameter)
                except AttributeError as e:
                    raise AttributeError(f"Missing attribute '{required_parameter}' for obj '{obj}'.") from e
                sigInfo[required_parameter] = attr_value

        return sigInfo.call()
    return wrapper_transfer(func, _wrapper)


def deco_extend(outer_cls):
    """ Allows additional arguments when inheriting and extending a built-in.
        Overrides __new__ to call cls' first base's __new__ with the single first given argument. """
    def __new__(cls, *args, **kwargs):
        arg = args[0] if args else next(iter(kwargs.values()))
        return cls.__bases__[0].__new__(cls, arg)

    outer_cls.__new__ = __new__
    return outer_cls


def deco_propagate_while(value, prop_func):
    """ Call decorated method recursively until it doesn't return given value. """
    def _deco(func):
        def _wrapper(self, *args, **kwargs):
            new_self = self
            while True:
                result = func(new_self, *args, **kwargs)
                if result != value:
                    break
                new_self = prop_func(new_self)
                if new_self is None:
                    break
            return result
        return wrapper_transfer(func, _wrapper)
    return _deco


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
    def deco_define_comparisons(cls, leftLambda, rightLambda=None):
        """ Define all comparision operators for this class.
            Provide two functions that take one value and returns left and right values.
            Will make class instances unhashable as the `__eq__` method is defined without defining `__hash__`.

            Stubs:
                def __eq__(self, other): ...
                def __gt__(self, other): ...
                def __lt__(self, other): ...
                def __ge__(self, other): ...
                def __le__(self, other): ... """
        if rightLambda is None:
            rightLambda = leftLambda

        def _wrapper(baseCls):
            for name, func in cls.comparisons.items():
                setattr(baseCls, name, lambda a, b, func=func: func(leftLambda(a), rightLambda(b)))

            return baseCls
        return _wrapper


def deco_require(assertion, *assert_args, message=None, default=None, **assert_kwargs):
    """ Decorator factory to produce decorate which raises AssertionError if assertion returns False.

        :param ((Any) -> bool) or bool assertion: Function that takes self and returns boolean.
        :param (function) -> str message: Function that takes wrapped function and returns error message.
        :param default: """
    def _deco(func):
        def _wrapper(*args, **kwargs):
            siginfo = SigInfo(func, *args, **kwargs)

            if callable(assertion):
                assertion_siginfo = SigInfo(assertion, *assert_args, *args, **assert_kwargs, **kwargs)
                result = assertion_siginfo.call()
            else:
                result = assertion

            if not result:
                if siginfo["error"] is False:
                    return default

                assertion_name = getattr(assertion, "__name__", assertion)

                if message is not None:
                    message_string = message(func=func)
                elif assertion_name == "<lambda>":
                    message_string = f"'{func.__name__}' cannot be called because deco_require failed."
                else:
                    message_string = f"'{func.__name__}' requires '{assertion_name}' function to be True."
                raise AssertionError(message_string)
            return siginfo.call()
        return _wrapper
    return _deco



























