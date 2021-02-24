
from generallibrary import *
from generalfile import Path




class A(TreeDiagram):
    def __init__(self, value, parent=None):
        self.value = value

    def __repr__(self):
        return str(self.value)

a = A(1)
b = a.add(2)
c = b.add(3)
d = a.add(4)
# print(d.get_ordered_index())
# print(a.get_children(-1))
# print(a.get_children(include_self=True, depth=3))


print(a.get_ordered())



















