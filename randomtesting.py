
from generallibrary import *

import sys
import inspect


# Todo: Idea: Use TreeDiagram in generalfile?

class Base:
    def hello(self):
        pass


class Foo(Base):
    bar = 5



objInfo = ObjInfo(Foo).get_parent()
objInfo.get_attrs(filter_func=lambda objInfo: not objInfo.private() and not objInfo.is_module(), depth=-1)
objInfo.view()






