
from generallibrary import *
from generalfile import Path




class A(NetworkDiagram):
    def __init__(self, value, parent=None):
        self.value = value

    def __repr__(self):
        return str(self.value)




a = A(1)
a.add(2)


# print(a.get_children())
# print(a.get_parents())
print(a.get_ordered())


































