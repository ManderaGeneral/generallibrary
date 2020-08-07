
from generallibrary.time import *
from generallibrary.types import *
from generallibrary.iterables import *
from generallibrary.functions import *
from generallibrary.object import *
from generallibrary.values import *

# from generalobjexp import ObjExp


class Base:
    def __init__(self, x):
        self.x = x

@initBases
class Parent(Base):
    def __init__(self, x):
        self.y = 5





# parent = Parent(1, 2, 3, z=8)
parent = Parent()

print(parent.x)




# SigInfo(lambda x: print(x), 1)()
