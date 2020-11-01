import inspect
import re
import functools


class SigInfo:
    """
    Handles a callable along with it's parameters.
    Forgiving as it sets missing values to None.
    Parameters can be changed but not callableObject.
    """
    def __init__(self, callableObject, *args, **kwargs):
        assert callable(callableObject)

        self._callableObject = callableObject

        # Stores *args and **kwargs indirectly in their own object if they exist
        self.allArgs = {}
        kwargs.update(self._argsToKwargs(list(args)))
        for name, value in kwargs.items():
            self[name] = value

    def _argsToKwargs(self, args):
        assert self.packedArgsName or len(args) <= len(self.positionalArgNames)

        kwargs = {}
        for i, (name, arg) in enumerate(zip(self.positionalArgNames, args)):
            if name == self.packedArgsName:
                kwargs[name] = args[i:]
                assert i + 1 == len(self.positionalArgNames)  # Make sure this is last iteration becuse *args should be last
            else:
                kwargs[name] = arg
        return kwargs

    @property
    def callableObject(self):
        """Propertize to protect but still have public"""
        return self._callableObject

    # ========= Level 1 - SIGNATURE PARAMETERS =========

    @property
    def parameters(self):
        """Get list of inspect parameter objects"""
        return inspect.signature(self.callableObject).parameters.values()

    @property
    def names(self):
        """Get list of parameter names"""
        return [param.name for param in self.parameters]

    @property
    def namesWithoutDefaults(self):
        """Get list of parameter names except those ones that have a default value"""
        return [name for name in self.names if name not in self.defaults]

    @property
    def namesRequired(self):
        """Get list of parameter that have to be defined, i.e. non-packed without default value"""
        return [name for name in self.names if name not in list(self.defaults.keys()) + [self.packedArgsName, self.packedKwargsName]]

    @property
    def namesWithoutPacked(self):
        """Get list of parameter names except *args or **kwargs"""
        return [name for name in self.names if name not in (self.packedArgsName, self.packedKwargsName)]

    @property
    def leadingArgNames(self):
        """
        Get names leading args that don't have default value.
        '*args' wont be included.
        'self' wont be included.
        """
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
        """Get name of packed *args or None"""
        for param in self.parameters:
            if param.kind.name == "VAR_POSITIONAL":
                return param.name

    @property
    def packedKwargsName(self):
        """Get name of packed *kwargs or None"""
        for param in self.parameters:
            if param.kind.name == "VAR_KEYWORD":
                return param.name

    @property
    def defaults(self):
        """Get dict of default values"""
        d = {param.name: param.default for param in self.parameters if param.default is not param.empty}

        if "self" in self.names and "self" not in d:
            d["self"] = self.callableObject

        return d

    @property
    def positionalArgNames(self):
        """
        Get list of parameter names that can take a positional argument.
        `*args` included but is always last if it exists.
        """
        return [param.name for param in self.parameters if param.kind.name in ("POSITIONAL_ONLY", "POSITIONAL_OR_KEYWORD", "VAR_POSITIONAL")]

    @property
    def keywordArgNames(self):
        """
        Get list of parameter names that can only take a keyword argument.
        Opposite of `self.positionalArgNames`.
        `**kwargs` included but is always last if it exists.
        """
        return [name for name in self.names if name not in self.positionalArgNames]

    def getIndexFromName(self, name):
        """Get index from name if name exists, else None"""
        if name in self.names:
            return self.names.index(name)

    # ========= Level 2 =========

    @property
    def definedNames(self):
        """Return list of names that are defined"""  # Not sure if keys in packedKwargsName should be included
        joinedLists = list(self.allArgs.keys()) + list(self.defaults.keys())
        # if self.packedKwargsName:
        #     joinedLists += list(self[self.packedKwargsName].keys())
        return [name for name in self.names if name in joinedLists]

    @property
    def requiredAreDefined(self):
        """Return whether required parameters are defined or not"""
        for name in self.namesRequired:
            if name not in self.definedNames:
                return False
        return True

    @property
    def unpackedArgs(self):
        """Return a list of all positional parameter values"""
        args = []
        for name in self.positionalArgNames:
            if name == self.packedArgsName:
                args.extend(self[self.packedArgsName])
            else:
                args.append(self[name])
        return args

    @property
    def unpackedKwargs(self):
        """Return a dict of parameters with their values excluding those in positionalArgNames / unpackedArgs"""
        kwargs = {}
        for name in self.keywordArgNames:
            if name == self.packedKwargsName:
                kwargs.update(self[self.packedKwargsName])
            else:
                kwargs[name] = self[name]
        return kwargs

    @property
    def unpackedAllArgs_without_missing(self):
        """ Return a dict with all parameters and their values.
            Entire *args and **kwargs objects will be included as well as unpacked **kwargs.
            Which means there are duplicate values if **kwargs is not empty. """
        kwargs = {}
        for name in self.names:
            if name in self.allArgs:
                kwargs[name] = self.allArgs[name]

                if name == self.packedKwargsName:
                    kwargs.update(self.allArgs[name])

            elif name in self.defaults:
                kwargs[name] = self.defaults[name]

        return kwargs

    @property
    def unpackedAllArgs(self):
        """
        Return a dict with all parameters and their values.
        Entire *args and **kwargs objects will be included as well as unpacked **kwargs.
        Which means there are duplicate values if **kwargs is not empty.
        Missing values are set to None.
        """
        kwargs = self.unpackedAllArgs_without_missing

        for name in self.names:
            if name not in kwargs:
                if name == self.packedArgsName:
                    kwargs[name] = []
                elif name == self.packedKwargsName:
                    kwargs[name] = {}
                else:
                    kwargs[name] = None

        return kwargs

    # ========= Level 3 =========

    def __getitem__(self, name):
        """Get value of a parameter from unpackedAllArgs, otherwise None."""
        if name in self.unpackedAllArgs:
            return self.unpackedAllArgs[name]

    def __setitem__(self, name, value):
        """Can set single key, entire *args, entire **kwargs or key inside **kwargs.
        If there's no place for key then it's ignored."""
        if name in self.names:
            if name == self.packedArgsName and not isinstance(value, (tuple, list)):
                raise AttributeError(f"Packed args parameter value has to be list or tuple.")
            if name == self.packedKwargsName and not isinstance(value, dict):
                raise AttributeError(f"Packed kwargs parameter value has to be a dict.")

            self.allArgs[name] = value

        elif self.packedKwargsName:
            addToDictInDict(self.allArgs, self.packedKwargsName, **{name: value})

    def __call__(self):
        """
        Calls callableObject with filled args and kwargs.
        Unfilled required parameters will get a None value
        """
        assert self.requiredAreDefined
        return self.callableObject(*self.unpackedArgs, **self.unpackedKwargs)

    def setParameters(self, **parameters):
        """Set parameters automatically in args or kwargs if the name exists in self.names."""
        for name, value in parameters.items():
            self[name] = value
        return self

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
    :param overwriteNone: Whether to overwrite None values or not.
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
                    SigInfo(leftLambda, left=left, right=right)(),
                    SigInfo(rightLambda, left=left, right=right)())
                setattr(baseCls, name, lambdaFunc)

            return baseCls
        return wrapper


def deco_cache():
    """ Enable caching for a method or function. """
    return functools.lru_cache()

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

            return sigInfo()
        return _wrapper
    return _decorator

def deco_default_self_args(func):
    """ As an alternative to setting each and every parameter's default value to `None` for a class method.
        Automatically sets each undefined parameter to self's attribute, which allows us to set a parameter `None`.
        Note: Parameters names must match attributes in self. """
    def _wrapper(*args, **kwargs):
        sigInfo = SigInfo(func, *args, **kwargs)

        defined_args = sigInfo.unpackedAllArgs_without_missing

        for required_parameter in sigInfo.namesRequired:
            if required_parameter not in defined_args:
                try:
                    attr_value = getattr(sigInfo["self"], required_parameter)
                except AttributeError:
                    raise AttributeError(f"Missing attribute '{required_parameter}' for instance '{sigInfo['self']}'.")
                sigInfo[required_parameter] = attr_value

        return sigInfo()
    return _wrapper


class EmptyContext:
    """ Class for an empty context manager. """
    def __enter__(self):
        pass
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


from generallibrary.iterables import addToDictInDict
from generallibrary.types import typeChecker
































