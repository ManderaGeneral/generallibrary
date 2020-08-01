
import sys

from types import ModuleType, FunctionType

from gc import get_referents

from generallibrary.functions import defaults, getSignatureDefaults, getSignatureNames


BLACKLIST = type, ModuleType, FunctionType
def getsize(obj):
    """
    Sum size of object & members.
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

def initBases(cls):
    """
    Automatically initalizes all inherited classes.
    Only allows class to be initiated with key word arguments. This is to prevent conflicts and to make it more intuitive.
    If a base has an argument without a default value then Parent must have that key word as argument itself

    TODO: Handle what happens if a Base requires *args or **kwargs -> Probably clean up library to get info regarding this too
    TODO: Handle Bases having same argument
    TODO: Probably allow *args as well

    :param cls:
    """
    clsInit = cls.__init__

    # Only allow **kwargs
    def __init__(self, **kwargs):
        kwargs["self"] = self

        # Add default values to kwargs unless they've been defined
        kwargs = defaults(kwargs, **getSignatureDefaults(clsInit))

        inits = [clsInit]
        for base in cls.__bases__:
            if base.__init__ == object.__init__:
                continue
            inits.insert(0, base.__init__)

        # for name in getSignatureNames(base.__init__, includeDefaulted=False):



        # Call all inits including cls' and check for excess args.
        usedArgs = []
        for init in inits:
            initKwargs = {}

            initDefaults = getSignatureDefaults(init)
            for name in getSignatureNames(init):

                if name not in kwargs:
                    # print(getSignatureNames(base.__init__, includeDefaulted=False))
                    raise AttributeError(f"Class '{cls.__name__}' is missing required key word argument '{name}' for base class '{init.__qualname__}'.")  # HERE **

                usedArgs.append(name)

                # Use default value of Base if the value in kwargs is None
                if kwargs[name] is None and name in initDefaults:
                    initKwargs[name] = initDefaults[name]
                else:
                    initKwargs[name] = kwargs[name]

            init(**initKwargs)

        for name in kwargs:
            if name not in usedArgs:
                raise AttributeError(f"Excess argument '{name}' for initializing '{cls.__name__}'.")

    cls.__init__ = __init__
    return cls




































