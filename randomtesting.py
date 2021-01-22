
from generallibrary import *

from itertools import chain


# HERE ** Rough sketch for NetworkDiagram, eventually combine with TreeDiagram to share inheritence

class Link:
    def __init__(self, base, target):
        self.base = base  # type: Node
        self.target = target  # type: Node

    def other_node(self, node):
        return self.base if self.target is node else self.target

    def __str__(self):
        return f"{self.base} -> {self.target}"
    __repr__ = __str__


class Node:
    def __init__(self, test):
        self.test = test
        self.links = []  # type: list[Link]

    def __str__(self):
        return str(self.test)
    __repr__ = __str__

    def link(self, target):
        link = Link(base=self, target=target)
        self.links.append(link)
        target.links.append(link)




    def _get_active_links(self, incoming, outgoing):
        return [link for link in self.links if (incoming and link.target is self) or (outgoing and link.base is self)]

    def _get_connected_nodes(self, route, incoming, outgoing):
        active_links = self._get_active_links(incoming=incoming, outgoing=outgoing)

        connected_nodes = []
        for link in active_links:
            other_node = link.other_node(self)
            if other_node not in route:
                connected_nodes.append(other_node)
        return connected_nodes

    def get_nodes(self, depth=1, incoming=True, outgoing=True, combined=True, _route=None):
        if _route is None:
            _route = []
        _route.append(self)

        if depth == 0:
            return _route

        connected_nodes = self._get_connected_nodes(route=_route, incoming=incoming, outgoing=outgoing)
        if connected_nodes:
            connected_nodes[0].get_nodes(depth=depth - 1, incoming=incoming, outgoing=outgoing, combined=combined, _route=_route)
        return _route


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.link(b)
b.link(c)
c.link(d)
d.link(b)

print(b.get_nodes(depth=-1))



