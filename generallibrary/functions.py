import inspect
import re


class SigInfo:
    """
    Get info regarding a signature.
    Also useful for handling decorators.
    Unforgiving as it sets missing values to None.
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
    def unpackedAllArgs(self):
        """
        Return a dict with all parameters and their values.
        Entire *args and **kwargs objects will be included as well as unpacked **kwargs.
        Which means there are duplicate values if **kwargs is not empty.
        Missing values are set to None.
        """
        kwargs = {}
        for name in self.names:
            if name in self.allArgs:
                kwargs[name] = self.allArgs[name]

                if name == self.packedKwargsName:
                    kwargs.update(self.allArgs[name])

            elif name in self.defaults:
                kwargs[name] = self.defaults[name]

            else:
                kwargs[name] = None
                # raise AttributeError(f"{name} doesn't exist in {self.allArgs} or {self.defaults}")

        return kwargs

    # ========= Level 3 =========

    def __getitem__(self, name):
        """Get value of a parameter from unpackedAllArgs, otherwise None."""
        if name in self.unpackedAllArgs:
            return self.unpackedAllArgs[name]

    def __setitem__(self, name, value):
        """Can set single key, entire *args, entire **kwargs or key inside **kwargs."""
        # if name not in self.names and self.packedKwargsName is None:
        #     raise AssertionError(f"Cannot set parameter '{name}' as there is no parameter with that name nor is there a packed kwargs parameter.")

        if name in self.allArgs:
            if name == self.packedArgsName and not isinstance(value, (tuple, list)):
                raise AttributeError(f"Packed args parameter value has to be list or tuple.")
            if name == self.packedKwargsName and not isinstance(value, dict):
                raise AttributeError(f"Packed kwargs parameter value has to be a dict.")

            self.allArgs[name] = value

        elif name in self.names:
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
    Taken from https://stackoverflow.com/questions/61948141/python-function-from-mathematical-expression-string/61949248
    """
    return re.findall(r"(\b\w*[.]?\w+\b|[()+*\-/])", expression)

def calculate(expression, *args):
    """
    Calculate function which can take any expression. Enter args in the order that they appear.
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
    Overwrite kwargs with dictionary.
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
    def defineComparisons(cls, leftLambda, rightLambda):
        """Define all comparision operators for this class.
        Provide two functions that return left and right values.
        Automatically fills 'left' and 'right' parameters by name."""
        def wrapper(baseCls):
            """."""
            for name, func in cls.comparisons.items():

                lambdaFunc = lambda left, right, func=func: func(
                    SigInfo(leftLambda, left=left, right=right)(),
                    SigInfo(rightLambda, left=left, right=right)())
                setattr(baseCls, name, lambdaFunc)

            return baseCls
        return wrapper



import importlib

def conditionallyImportInheritence(condition, module, cls):
    if condition:
        importlib.import_module(module)



from generallibrary.iterables import addToDictInDict
































