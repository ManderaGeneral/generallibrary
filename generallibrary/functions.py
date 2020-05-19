
import inspect

def leadingArgsCount(func):
    """
    Get number of leading args without a default value.

    :param function func: Generic function
    """
    count = 0
    for _, value in inspect.signature(func).parameters.items():
        if value.default is inspect.Parameter.empty:
            count += 1
        else:
            break
    return count

def getSignatureNames(cls):
    """
    Get a callable class' signature paramaeter keys as a tuple.

    :param type cls: Generic callable class
    :rtype: tuple[str]
    """
    return tuple(inspect.signature(cls).parameters.keys())
