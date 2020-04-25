import traceback
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
    def __init__(self, startDT = None):
        if startDT is None:
            self.time = dt.datetime.now()
        else:
            if not isinstance(startDT, dt.datetime):
                raise TypeError(f"{startDT} is not a datetime object")
            self.time = startDT

    def seconds(self):
        """
        :return: Seconds passed since timer started
        :rtype: float
        """
        return (dt.datetime.now() - self.time).seconds

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
        else:
            return depth

def typeChecker(obj, fullIteration=False, raiseTypeError=True, *types):
    try:
        if not types:
            raise TypeError("No types were given as args")
        objDepth = depth(obj)
        typesDepth = len(types) - 1
        if objDepth != typesDepth:
            raise TypeError(f"Obj depth {objDepth} doesnt match types len {len(types)}")

        for i, argType in enumerate(types):
            if not isinstance(obj, argType):
                raise TypeError(f"obj {obj} wasn't type {argType} in depth {i} / {typesDepth}")

            if iterable(obj):
                obj = iterFirstValue(obj)
            elif i < objDepth:
                raise TypeError(f"obj {obj} is not iterable but atleast one more subtype is required in depth {i} / {typesDepth}")

    except TypeError as e:
        if raiseTypeError:
            raise e
        else:
            return False
    else:
        return True










































