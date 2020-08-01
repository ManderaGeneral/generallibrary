
from generallibrary.time import *
from generallibrary.types import *
from generallibrary.iterables import *
from generallibrary.functions import *
from generallibrary.object import *

from generalobjexp import ObjExp





class Base:
    def test(self):
        pass
    # def __init__(self, x, z):
    #     self.x = x
    #     self.z = z

@initBases
class Parent(Base):
    def __init__(self, x):
        self.y = 2

Parent()



# def x(self, *args, **kwargs):
#     pass


# def test(a, x=5, *args, **kwargs):
#     pass
# for key, value in inspect.signature(test).parameters.items():
#     print(value.kind)































