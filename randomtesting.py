
from generallibrary import *


@initBases
class Node(NetworkDiagram):
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return str(self.x)



a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

# a.link(b)
# b.link(c)
# c.link(d)
# d.link(b)
# c.link(e)


a.link(c)
b.link(c)
c.link(d)
c.link(e)
e.link(f)


print(a.get_ordered_dict())





