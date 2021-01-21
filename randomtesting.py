
from generallibrary import *

from itertools import chain


# HERE ** Rough sketch for NetworkDiagram, eventually combine with TreeDiagram to share inheritence

class _Link:
    def __init__(self, base, target):
        self.base = base
        self.target = target

    def __str__(self):
        return f"{self.base} -> {self.target}"
    __repr__ = __str__


class Node:
    def __init__(self, test):
        self.test = test
        self.links = set()  # type: set[_Link]

    def __str__(self):
        return str(self.test)
    __repr__ = __str__

    def link(self, target):
        link = _Link(base=self, target=target)
        self.links.add(link)
        target.links.add(link)

    def connected_node(self, link):
        return link.base if link.target is self else link.target

    def nodes(self):
        return {self.connected_node(link=link) for link in self.links}

    def all_links(self):
        return set().union(*[node.links for node in self.all_nodes()])

    def all_nodes(self):
        nodes = set()
        queued_nodes = {self}
        while queued_nodes:
            nodes.update(queued_nodes)
            connected_to_queued = set().union(*[node.nodes() for node in queued_nodes])
            queued_nodes = connected_to_queued - nodes
        return nodes


a = Node(1)
b = Node(2)
c = Node(3)

a.link(b)
b.link(c)
c.link(a)

print(a.all_links())
print(a.all_nodes())



