
import generallibrary
from generallibrary import *

import sys
import inspect



# Todo: Idea: Use TreeDiagram in generalfile?

class Base:
    def hello(self):
        pass


class Foo(Base):
    bar = 5



# print(TreeDiagram.__weakref__.__name__)
# exit()

objInfo = ObjInfo(generallibrary)

# objInfo.get_attrs(filter_func=False)
# objInfo.view(custom_repr=lambda x: f"{str(x):<50}{x.get_parent().cls.__module__}")

objInfo.filters.append(lambda x: not x.is_module())
objInfo.get_attrs(depth=-1)
objInfo.view()






