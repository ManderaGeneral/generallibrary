
from generallibrary import *
from generalfile import Path




class A(NetworkDiagram):
    def __init__(self, value, parent=None):
        self.value = value

    def __repr__(self):
        return str(self.value)



a = A(1)
b = a.add(2)
c = a.add(3)
c.set_parent(4)

print(a.get_spouses())
print(c.get_siblings())





































