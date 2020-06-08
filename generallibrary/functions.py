
import inspect
import re

def leadingArgsCount(func):
    """
    Get number of leading args without a default value.

    :param function func: Generic function
    """
    count = 0
    for _, value in inspect.signature(func).parameters.items():
        if value.default is inspect.Parameter.empty and value.kind.name == "POSITIONAL_OR_KEYWORD" and value.name != "self":
            count += 1
    return count

def getSignatureNames(cls):
    """
    Get a callable class' or func's signature parameter keys as a tuple.

    :param type cls: Generic callable class
    :rtype: list[str]
    """
    return list(inspect.signature(cls).parameters.keys())


def changeArgsAndKwargs(func, args, kwargs, **newParameters):
    args = list(args)

    parameters = getSignatureNames(func)
    if "self" in parameters:
        parameters.remove("self")

    for name, value in newParameters.items():
        if name in parameters:
            index = parameters.index(name)
        else:
            index = None

        if index is not None and len(args) > index:
            args[index] = value
        else:
            kwargs[name] = value

    return tuple(args), kwargs



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