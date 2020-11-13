
from generallibrary import *

# print(getLocalFeaturesAsMD(locals(), "generallibrary"))



class A:
    def __init__(self):
        print(1)
        self.testing = 5

@initBases
class B(A):
    def __init__(self):
        print(2)



B()
