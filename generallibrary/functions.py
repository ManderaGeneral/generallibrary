
import inspect
import re




class SigInfo:
    """
    Get info regarding a signature.
    Also useful for handling decorators.
    """
    def __init__(self, callableObject, args=None, kwargs=None):
        """
        :param callableObject:
        :param tuple args:
        :param dict kwargs:
        """
        assert callable(callableObject)

        self.callableObject = callableObject
        self.args = [] if args is None else list(args)
        self.kwargs = {} if kwargs is None else kwargs.copy()

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
    def defaults(self):
        """Get dict of default values"""
        return {param.name: param.default for param in self.parameters if param.default is not param.empty}

    @property
    def leadingArgs(self):
        """Get names leading args that don't have default value"""
        leadingArgs = []
        for param in self.parameters:
            if param.default is inspect.Parameter.empty and param.kind.name == "POSITIONAL_OR_KEYWORD" and param.name != "self":
                leadingArgs.append(param.name)
        return leadingArgs

    @property
    def packedArgs(self):
        """Get names of all *args"""
        return [param.name for param in self.parameters if param.kind == "VAR_POSITIONAL"]

    @property
    def packedKwargs(self):
        """Get names of all *kwargs"""
        return [param.name for param in self.parameters if param.kind == "VAR_KEYWORD"]


    def getIndexFromName(self, name):
        """."""
        return self.names.index(name) if name in self.names else None

    def getParameter(self, name):
        """Get value of a parameter from args or kwargs if it exists, otherwise None"""
        index = self.getIndexFromName(name)

        if index is not None and len(self.args) > index:
            # Args
            return self.args[index]
        else:
            # Kwargs
            if name in self.kwargs:
                return self.kwargs[name]

            # Default
            if name in self.defaults:
                return self.defaults[name]

            # Doesn't exist at all
            return None

    def setParameters(self, **parameters):
        """Set parameters automatically in args or kwargs."""
        for name, value in parameters.items():
            index = self.getIndexFromName(name)

            if index is not None and len(self.args) > index:
                self.args[index] = value
            else:
                self.kwargs[name] = value
        return self

    def __call__(self):
        return self.callableObject(*self.args, **self.kwargs)



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





































