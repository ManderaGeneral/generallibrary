
import sys

from types import ModuleType, FunctionType

from gc import get_referents


BLACKLIST = type, ModuleType, FunctionType
def getsize(obj):
    """
    Get a sum of sizes from an object and it's members in bytes.
    Custom objects know their class.
    Function objects seem to know way too much, including modules.
    Exclude modules as well.

    Author: Aaron Hall @ https://stackoverflow.com/questions/449560/how-do-i-determine-the-size-of-an-object-in-python
    """
    if isinstance(obj, BLACKLIST):
        # raise TypeError('getsize() does not take argument of type: '+ str(type(obj)))
        return sys.getsizeof(obj)
    seen_ids = set()
    size = 0
    objects = [obj]
    while objects:
        need_referents = []
        for obj in objects:
            if not isinstance(obj, BLACKLIST) and id(obj) not in seen_ids:
                seen_ids.add(id(obj))
                size += sys.getsizeof(obj)
                need_referents.append(obj)
        objects = get_referents(*need_referents)
    return size

def getClassFromMethod(method):
    """
    Retrieve class object from a method object.

    :param function method:
    :rtype: type
    """
    splitQualname = method.__qualname__.split('.')
    if len(splitQualname) != 2:
        raise AttributeError(f"{method} is probably not a method")

    return getattr(sys.modules[method.__module__], splitQualname[0])

def attributes(obj):
    """Get all attributes of an object that don't start with `__`, as a dictionary."""
    attrs = {}
    for key in dir(obj):
        attr = getattr(obj, key)
        classAttr = getattr(obj.__class__, key, None)

        if not key.startswith("__") and not callable(classAttr) and not isinstance(classAttr, property):
            attrs[key] = attr
    return attrs

def initBases(cls):
    """
    Decorator function for class to automatically initalize all inherited classes.
    If a base has an argument without a default value then Parent must have that key word as argument itself
    """
    clsInit = cls.__init__

    def __init__(*args, **kwargs):
        clsSigInfo = SigInfo(clsInit, *args, **kwargs)

        for base in list(cls.__bases__) + [cls]:
            baseInit = clsInit if base == cls else base.__init__
            if baseInit != object.__init__:
                sigInfo = SigInfo(baseInit)

                for name in sigInfo.names:
                    if clsSigInfo[name] is None and sigInfo[name] is not None:  # Call continue to not overwrite with a None value
                        continue
                    assert name in clsSigInfo.definedNames
                    sigInfo[name] = clsSigInfo[name]

                sigInfo()

    cls.__init__ = __init__
    return cls


from generallibrary.functions import SigInfo


































