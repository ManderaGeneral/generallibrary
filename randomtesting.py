
from generallibrary.time import *
from generallibrary.types import *
from generallibrary.iterables import *
from generallibrary.functions import *
from generallibrary.object import *

from generalobjexp import ObjExp





class Base:
    def __init__(self, *x):
        self.x = x

@initBases
class Parent(Base):
    def __init__(self, x):
        self.y = 2

    def hi(self):
        pass


# print(getSignatureArgs(Base.__init__))

# print(Parent(x=2))

































