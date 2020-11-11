
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

    Wrap a class' unbound __init__ method to take any arguments.
    When wrapper is called it iterates DIRECT bases to call their unbound __init__ methods along with it's own original __init__.

    """
    cls_init = cls.__init__  # Unbound original __init__ method of class

    def _wrapper(*args, **kwargs):
        cls_SigInfo = SigInfo(cls_init, *args, **kwargs)

        initialized_bases = []
        for init in [base.__init__ for base in cls.__bases__] + [cls_init]:
            if init is not object.__init__ and init not in initialized_bases:
                cls_SigInfo(child_callable=init)
                initialized_bases.append(init)

    cls.__init__ = _wrapper
    return cls


from generallibrary.functions import SigInfo


































