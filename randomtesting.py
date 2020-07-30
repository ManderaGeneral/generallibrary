
from generallibrary.time import *
from generallibrary.types import *
from generallibrary.iterables import *
from generallibrary.functions import *

from generalobjexp import ObjExp




def initBases(cls):
    """
    Automatically initalizes all inherited classes.
    Only allows class to be initiated with key word arguments. This is to prevent conflicts and to make it more intuitive.

    :param cls:
    """
    clsInit = cls.__init__

    # Only allow **kwargs
    def __init__(self, **kwargs):
        kwargs["self"] = self
        kwargs = defaults(kwargs, **getSignatureDefaults(clsInit))

        inits = [clsInit]
        for base in cls.__bases__:
            for name in getSignatureNames(base.__init__, includeDefaulted=False):
                if name not in kwargs:
                    raise AttributeError(f"Class '{cls.__name__}' is missing required key word argument '{name}' for base class '{base.__name__}'.")

            inits.insert(0, base.__init__)

        # Call all inits including cls'.
        for init in inits:
            init(**{name: kwargs[name] for name in getSignatureNames(init)})

    cls.__init__ = __init__
    return cls


# TODO: Raise error if excess argument is given
# TODO: Handle what happens if a Base requires *args or **kwargs -> Probably clean up library to get info regarding this too
# TODO: Handle Base class without __init__
# TODO: Handle Bases having same argument



class Base:
    def __init__(self, x, z=3):
        self.x = x
        self.z = z

@initBases
class Parent(Base):
    def __init__(self, x, z=None):
        self.y = 2

print(Parent(x=5).z)

# print(Parent(x=5).z)













































