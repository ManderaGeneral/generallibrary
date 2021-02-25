
from generallibrary import *
from generalfile import Path




class A(TreeDiagram):
    def __init__(self, value, parent=None):
        self.value = value

    def __repr__(self):
        return str(self.value)

# a = A(1)
# b = a.add(2)
# c = b.add(3)
# d = a.add(4)




