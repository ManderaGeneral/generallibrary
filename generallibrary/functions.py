
import inspect
import re


class SigInfo:
    """
    Get info regarding a signature.
    Also useful for handling decorators.
    """
    def __init__(self, callableObject, *args, **kwargs):
        assert callable(callableObject)
        if len(self.packedKwargNames) > 1 or len(self.packedArgNames) > 1:
            raise NotImplementedError

        self.callableObject = callableObject
        # self.args = [] if args is None else list(args)
        # self.kwargs = {} if kwargs is None else kwargs.copy()


        self.allArgs = {}

        # Normal arg
        for i, name in enumerate(self.leadingArgNames):
            if i >= len(args):
                break
            self.allArgs[name] = args[i]

        # Extract *args
        if len(args) > len(self.leadingArgNames):
            if not self.packedArgNames:
                raise AttributeError("Too many args without a packed *args parameter")

            self.allArgs[self.packedArgNames[0]] = args[len(self.leadingArgNames):]

        if self.packedKwargNames:
            self.allArgs[self.packedKwargNames[0]] = {}

        for name, value in kwargs.items():
            # Normal kwarg
            if name in self.names:
                self.allArgs[name] = value

            # Extract **kwargs
            else:
                if not self.packedKwargNames:
                    raise AttributeError("Too many kwargs without a packed **kwargs parameter")
                self.allArgs[self.packedKwargNames[0]][name] = value


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
        return [param.name for param in self.parameters if param.name not in self.defaults]

    @property
    def namesWithoutPacked(self):
        """Get list of parameter names except *args or **kwargs"""
        return [param.name for param in self.parameters if param.name not in (self.packedArgNames + self.packedKwargNames)]

    @property
    def packedArgNames(self):
        """Get names of all *args"""
        return [param.name for param in self.parameters if param.kind.name == "VAR_POSITIONAL"]

    @property
    def packedKwargNames(self):
        """Get names of all *kwargs"""
        return [param.name for param in self.parameters if param.kind.name == "VAR_KEYWORD"]

    @property
    def leadingArgNames(self):
        """
        Get names leading args that don't have default value.
        '*args' wont be included.
        """
        leadingArgNames = []
        for param in self.parameters:
            if param.default is inspect.Parameter.empty and param.kind.name == "POSITIONAL_OR_KEYWORD" and param.name != "self":
                leadingArgNames.append(param.name)
        return leadingArgNames

    @property
    def defaults(self):
        """Get dict of default values"""
        d = {param.name: param.default for param in self.parameters if param.default is not param.empty}
        if "self" in self.names and "self" not in d:
            d["self"] = self.callableObject
        return d

    @property
    def filledArgs(self):
        """Return a list of all positional parameter values"""
        args = []
        for name in self.leadingArgNames:
            args.append(self[name])
        for packedArgName in self.packedArgNames:
            args.extend(self[packedArgName])
        return args

    @property
    def filledKwargs(self):
        """Return a list of all parameter values excluding those in leadingArgNames"""
        kwargs = {}
        for name in self.namesWithoutPacked:
            kwargs[name] = self[name]
        for packedKwargName in self.packedKwargNames:
            kwargs.update(self[packedKwargName])
        return {name: value for name, value in kwargs.items() if name not in self.leadingArgNames}

    @property
    def unpackedAllArgs(self):
        """Return allArgs but with packedKwargs removed and unpacked if it exists"""
        kwargs = self.allArgs.copy()
        if self.packedKwargNames:
            kwargs.update(kwargs[self.packedKwargNames[0]])
            del kwargs[self.packedKwargNames[0]]
        return kwargs

    def getIndexFromName(self, name):
        """Get index from name if name exists, else None"""
        if name in self.names:
            return self.names.index(name)

    def setParameters(self, /, **parameters):
        """Set parameters automatically in args or kwargs if the name exists in self.names."""
        for name, value in parameters.items():
            if name in self.names:
                self[name] = value
        return self

    def applyDefaults(self):
        """Replace all None or undefined parameters with default values"""
        for name, value in self.defaults.items():
            if self[name] is None:
                self[name] = value

    def copy(self):
        """Return a copy of this SigInfo"""
        return SigInfo(**attributes(self))

    def validParameters(self):
        """Check if a call can be made by checking all if all required parameters are defined"""
        for name in self.names:
            if name in self.packedKwargNames:
                continue
            if name in self.packedArgNames:
                continue
            if name in self.defaults:
                continue
            if self[name] is None:
                raise AttributeError(f"{self} does not have valid parameters, it's missing {name}")

    def __getitem__(self, name):
        """Get value of a parameter from unpackedAllArgs, otherwise None"""
        if name in self.unpackedAllArgs:
            return self.unpackedAllArgs[name]

        # Default
        elif name in self.defaults:
            return self.defaults[name]

        # Doesn't exist at all
        else:
            return None

    def __setitem__(self, name, value):
        index = self.getIndexFromName(name)
        # HERE ** Use unpackedAllArgs
        # if name in self.packedArgNames:
        #     assert isinstance(value, (list, tuple))
        #     self.args =

        if index is not None and len(self.args) > index:
            self.args[index] = value
        else:
            if name not in self.names and not self.packedKwargNames:
                raise AttributeError(f"Cannot set '{name}' because there's no parameter with that name")

            self.kwargs[name] = value

    def __call__(self):
        """
        Calls callableObject with filled args and kwargs.
        Unfilled required parameters will get a None value
        """
        # sigInfo = self.copy()
        # sigInfo.applyDefaults()
        # print(sigInfo.args, sigInfo.kwargs)
        # return sigInfo.callableObject(**{name: sigInfo[name] for name in sigInfo.names})
        self.validParameters()
        return self.callableObject(*self.filledArgs, **self.filledKwargs)  # If we do this then we wont need to copy

    def __repr__(self):
        return f"<SigInfo for '{self.callableObject.__class__.__name__}' with names '{', '.join(self.names)}'>"



ignore = ["+", "-", "*", "/", "(", ")", "sqrt"]
def _tokenize(expression):
    """
    Tokenize an expression
    Taken from https://stackoverflow.com/questions/61948141/python-function-from-mathematical-expression-string/61949248
    """
    return re.findall(r"(\b\w*[\.]?\w+\b|[\(\)\+\*\-\/])", expression)

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




from generallibrary.object import attributes
































