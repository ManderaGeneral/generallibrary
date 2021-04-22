
from generallibrary import *



class A(NetworkDiagram):
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return str(self.x)


a = A("a")
b = a.add_node("b")
c = b.add_node("c")
c.add_node(a)

d = c.add_node("d")
d.add_node(a)


print(a.graph())



