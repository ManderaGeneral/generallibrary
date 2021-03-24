
from generallibrary import *
from generalfile import Path

from pprint import pprint



class A(TreeDiagram):
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return str(self.x)


a = A(1)
b = a.add_node(2)
c = b.add_node(3)


# print(a.get_children(depth=-1, filt=lambda x: x.x != 2))


