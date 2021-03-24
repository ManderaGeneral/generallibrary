
from generallibrary import *
from generalfile import Path

from pprint import pprint





class A:
    def b(self):
        pass

    def c(self):
        pass


objInfo = ObjInfo(A)

objInfo.view(spawn=True, filt=lambda x: x.name != "c")

