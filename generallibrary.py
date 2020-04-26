import time
import datetime as dt

from math import *

def sleep(seconds):
    """
    Could do a sweet loading animation in console
    """
    time.sleep(seconds)

def dictFirstValue(dictionary):
    if not isinstance(dictionary, dict):
        raise TypeError("Not dictionary")
    if not len(dictionary):
        return None
    return dictionary[list(dictionary.keys())[0]]

def iterFirstValue(obj):
    if not iterable(obj):
        raise TypeError("obj is not iterable")
    if isinstance(obj, tuple) or isinstance(obj, list):
        return obj[0]
    elif isinstance(obj, dict):
        return dictFirstValue(obj)

def strToDynamicType(var):
    if var == "true" or var == "True":
        return True
    if var == "false" or var == "False":
        return False

    try:
        return int(var)
    except:
        pass

    try:
        return float(var)
    except:
        pass

    return var

class Timer:
    """
    Callable class to easily time things and print
    """
    def __init__(self, perfCounter = None):
        if perfCounter is None:
            self.perfCounter = time.perf_counter()
        else:
            typeChecker(perfCounter, float)
            self.perfCounter = perfCounter

    def seconds(self):
        """
        :return: Seconds passed since timer started
        :rtype: float
        """
        return time.perf_counter() - self.perfCounter

def iterable(obj):
    if isinstance(obj, tuple):
        return obj
    elif isinstance(obj, list):
        return obj
    elif isinstance(obj, dict):
        return obj.values()
    else:
        return None

def depth(obj):
    depth = 0
    while True:
        if iterable(obj):
            obj = iterFirstValue(obj)
            depth += 1
        else:
            return depth

def typeChecker(obj, *types, fullIteration=False, raiseTypeError=True):
    """
    Check types of an obj. Intended for iterables with somewhat consistent structure in every layer.
    :param obj:
    :param types:
    :param fullIteration:
    :param raiseTypeError:
    :return:
    """
    try:
        if not types:
            raise TypeError("No types were given as args")
        objDepth = depth(obj)
        typesDepth = len(types) - 1
        if objDepth != typesDepth:
            raise TypeError(f"Obj depth {objDepth} doesnt match types depth {typesDepth}")

        for i, argType in enumerate(types):
            if not isinstance(obj, argType):
                raise TypeError(f"obj {obj} wasn't type {argType} in depth {i}/{typesDepth}")

            if iterable(obj):
                obj = iterFirstValue(obj)
            elif i < objDepth:
                raise TypeError(f"obj {obj} is not iterable but atleast one more subtype is required in depth {i}/{typesDepth}")

    except TypeError as e:
        if raiseTypeError:
            raise e
        else:
            return False
    else:
        return True










































