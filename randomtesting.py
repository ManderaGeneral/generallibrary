
from generallibrary import *
from generalfile import Path

from pprint import pprint


# ObjInfo(Path).view(spawn=True)

print(len(ObjInfo(Path).get_children()))
print(len(ObjInfo(Path).get_children(-1)))




# class A(TreeDiagram):
#     def __init__(self, x):
#         self.x = x
#
#     def __repr__(self):
#         return str(self.x)
#
#
# a = A(1)
# b = a.add_node(2)
# c = b.add_node(3)
#
# b.disconnect(lambda node: node.x == 3)
#
# print(a.get_all())

