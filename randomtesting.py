
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

a.link(b)
b.link(c)
c.link(d)
d.link(b)
c.link(e)

print(b.get_routes(depth=1, outgoing=False).get_links())

# print(b.get_link(a))
# print(a.get_link(b))







