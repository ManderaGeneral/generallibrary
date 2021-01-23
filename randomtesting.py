
from generallibrary import *


# HERE ** Add methods to get nodes and links easily from Route
# Combine with TreeDiagram to share inheritence

class Route(list):
    """ List of nodes. """
    def copy(self):
        return Route(self)

    def is_circular(self):
        return self[-1] in self

    def is_uturn(self):
        return len(self) > 2 and self[-1] is self[-3]

    def __repr__(self):
        return f"{type(self).__name__}: {super().__repr__()}{' ⟲' * self.is_circular()}{' ⮌' * self.is_uturn()}"


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
            # if other_node not in route:
            connected_nodes.append(other_node)
        return connected_nodes

    def get_routes(self, depth=-1, incoming=False, outgoing=True, _route=None, _all_routes=None):
        """ Get a list of routes. """
        if _route is None:
            _route = Route()
            _all_routes = [_route]

        _route.append(self)
        if depth == 0 or _route.count(self) > 1:
            return _all_routes

        connected_nodes = self._get_connected_nodes(route=_route, incoming=incoming, outgoing=outgoing)
        _original_route = _route.copy()
        for i, node in enumerate(connected_nodes):
            if i == 0:
                new_route = _route
            else:
                new_route = _original_route.copy()
                _all_routes.append(new_route)
            node.get_routes(depth=depth - 1, incoming=incoming, outgoing=outgoing, _route=new_route, _all_routes=_all_routes)
        return _all_routes


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.link(b)
b.link(c)
c.link(d)
d.link(b)

print(a.get_routes())






