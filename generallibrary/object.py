
import sys
from types import ModuleType, FunctionType
from gc import get_referents
import inspect


def getsize(obj):
    """
    Get a sum of sizes from an object and it's members in bytes.
    Custom objects know their class.
    Function objects seem to know way too much, including modules.
    Exclude modules as well.

    Author: Aaron Hall @ https://stackoverflow.com/questions/449560/how-do-i-determine-the-size-of-an-object-in-python
    """
    _BLACKLIST = type, ModuleType, FunctionType
    if isinstance(obj, _BLACKLIST):
        # raise TypeError('getsize() does not take argument of type: '+ str(type(obj)))
        return sys.getsizeof(obj)
    seen_ids = set()
    size = 0
    objects = [obj]
    while objects:
        need_referents = []
        for obj in objects:
            if not isinstance(obj, _BLACKLIST) and id(obj) not in seen_ids:
                seen_ids.add(id(obj))
                size += sys.getsizeof(obj)
                need_referents.append(obj)
        objects = get_referents(*need_referents)
    return size


def initBases(cls):
    """
    Decorator function for class to automatically initalize all inherited classes.

    Wrap a class' unbound __init__ method to take any arguments.
    When wrapper is called it iterates DIRECT bases to call their unbound __init__ methods along with it's own original __init__.

    Also looks for defined `__init_post__` methods, stores them in `instance.__init_post__s` and calls them all after all inits.
    """
    cls_init = cls.__init__  # Unbound original __init__ method of class

    cls._is_wrapped_by_initBases = cls

    def _wrapper(*args, **kwargs):
        cls_SigInfo = SigInfo(cls_init, *args, **kwargs)

        if not cls_SigInfo["self"]:
            raise AttributeError(f"{cls} hasn't defined it's `__init__`")

        initialized_bases = []

        if getattr(cls_SigInfo["self"], "__init_post__s", None) is None:
            cls_SigInfo["self"].__init_post__s = []


        for base in cls.__bases__ + (cls, ):
            init = cls_init if base is cls else base.__init__

            if init is not object.__init__ and init not in initialized_bases:
                cls_SigInfo.call(child_callable=init)
                initialized_bases.append(init)


                if getattr(base, "__init_post__", None) and base.__init_post__ not in cls_SigInfo["self"].__init_post__s:
                    cls_SigInfo["self"].__init_post__s.append(base.__init_post__)
        if cls is cls_SigInfo["self"].__class__ and getattr(cls_SigInfo["self"], "__init_post__s", None) is not None:
            for post_init in cls_SigInfo["self"].__init_post__s:
                cls_SigInfo.call(child_callable=post_init)

    cls.__init__ = _wrapper
    return cls


from generallibrary.functions import SigInfo
from generallibrary.objinfo.objinfo import ObjInfo





