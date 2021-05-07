import pickle

from generallibrary import *

# from generalpackager import Packager
# Packager().graph()



class A(NetworkDiagram):
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return str(self.x)

# process = A("generalprocess")
# vector = A("generalvector")
# neural = A("generalneural")
# neat = A("generalneat")
# gui = A("generalgui")
# draw = A("generaldraw")
# stock = A("generalstock")
# analyze = A("generalanalyze")
# actioneer = A("generalactioneer")
#
# process.add_node(stock)
# process.add_node(analyze)
# process.add_node(stock)
#
# vector.add_node(draw)
# vector.add_node(gui)
#
# neural.add_node(neat)
#
# neat.add_node(actioneer)
#
# gui.add_node(analyze)
# gui.add_node(draw)
# gui.add_node(neural)
# gui.add_node(neat)
# gui.add_node(actioneer)
# gui.add_node(stock)
#
# draw.add_node(neural)
# draw.add_node(neural)
#
# stock.add_node(actioneer)
#
# analyze.add_node(stock)
# analyze.add_node(neural)
#
# actioneer.graph()


# Must be missing something, blocked nodes might not be right


# 3 Triangles in grid
# a = A("a")
# b = a.add_node("b")
# c = b.add_node("c")
# d = c.add_node("d")
# e = d.add_node("e")
# a.add_node(c)
# b.add_node(d)
# b.add_node(e)


# Square with triangle inside
# a = A("a")
# b = a.add_node("b")
# c = b.add_node("c")
# d = c.add_node("d")
# d.add_node(a)
# e = a.add_node("e")
# e.add_node(d)


# Pentagon with square inside
# a = A("a")
# b = a.add_node("b")
# c = b.add_node("c")
# d = c.add_node("d")
# e = d.add_node("e")
# e.add_node(a)
# f = e.add_node("f")
# f.add_node(c)


# 3 Triangles with 1 center node
a = A("a")
b = a.add_node("b")
c = b.add_node("c")
d = c.add_node("d")
c.add_node(a)
a.add_node(d)
b.add_node(d)


a.graph()



# loops = a.get_loops()
# small = loops[0]
# big = loops[1]
# assert len(small.nodes) < len(big.nodes)

# big.add_node(child=small)
# print(big.unavailable_nodes())
# print(small.unavailable_nodes())
# print(big.all_nodes())

# print(big.can_contain(small))
# print(small.can_contain(big))


# a = A("a")
# b = a.add_node("b")
# c = b.add_node("c")
# c.add_node(a)
#
# d = c.add_node("d")
# d.add_node(a)
#
#
# print(a.graph())



