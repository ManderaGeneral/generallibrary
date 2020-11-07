
from generallibrary import *

# print(getLocalFeaturesAsMD(locals(), "generallibrary"))




class C:
    def __init__(self, a):
        self.a = a

@initBases
class B(C):
    def __init__(self):
        pass

@initBases
class A(B):
    def __init__(self, a=None):
        pass


print(A().a)
