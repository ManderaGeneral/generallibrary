
import generallibrary
from generallibrary import *

import sys
import inspect


class Base:
    def hello(self):
        pass


class Foo(Base):
    bar = 5




objInfo = ObjInfo(Foo)
objInfo.get_attrs()

objInfo.view()
objInfo.get_child().set_index(1)
objInfo.view()



