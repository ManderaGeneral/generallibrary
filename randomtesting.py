
from generallibrary import *
from generalfile import Path

import generallibrary


from itertools import chain


def flatten_gen(list_):
    yield from (item for items in list_ for item in items)


def flatten(list_):
    return list(flatten_gen(list_=list_))


def _extend_unique(total, add):
    unique = [item for item in add if item not in total]
    total.extend(unique)
    return unique


def _traverse_depth(*nodes, func, depth, _all_nodes=None):
    if depth is None:
        depth = 0
    if _all_nodes is None:
        _all_nodes = []

    results = [node2 for node1 in nodes for node2 in func(node1) if node2 not in _all_nodes]
    if results:
        yield results
        _all_nodes.extend(results)
        if depth != 0:
            yield from _traverse_depth(*results, func=func, depth=depth - 1, _all_nodes=_all_nodes)


def _deco_depth(func):
    def _wrapper(node, depth=None):
        yield from _traverse_depth(node, func=func, depth=depth)
    return _wrapper


def _deco_cast_to_diagram(func):
    """ Allows first arg to be same type as self or the args the create a new one. """
    def _wrapper(self, *args, **kwargs):
        combined = args + tuple(kwargs.values())
        if combined and (combined[0] is None or type(combined[0]) == type(self)):
            diagram = combined[0]
        else:
            diagram = type(self)(*args, **kwargs)
        return func(self, diagram)
    return _wrapper



class _Diagram_QOL:
    """ Quality of life helper methods of Diagram. """
    def view(self):
        pass

    def get_children(self, depth=None):
        return flatten(self.get_children_gen(depth=depth))

    def get_parents(self, depth=None):
        return flatten(self.get_parents_gen(depth=depth))

    def get_nodes(self, depth=None):
        return flatten(self.get_nodes_gen(depth=depth))

    def get_siblings(self, depth=None):
        return flatten(self.get_siblings_gen(depth=depth))


class _NetworkDiagram_QOL:
    """ Quality of life helper methods of _NetworkDiagram_QOL. """
    def get_spouses(self, depth=None):
        return flatten(self.get_spouses_gen(depth=depth))


class _TreeDiagram_QOL:
    """ Quality of life helper methods of _TreeDiagram_QOL. """
    def get_parent(self, depth=None):
        return get(self.get_parents(depth=depth), depth)


class _Diagram_Global:
    """ Core global methods of a Diagram. """
    def get_ordered_gen(self):
        origins = []
        for node in self.get_nodes_gen(depth=-1):
            if not node.get_parents():
                origins.append(node)
        yield origins
        yield from _traverse_depth(*origins, func=self.get_children_gen.__func__, depth=-1)

    def get_ordered(self):
        return list(self.get_ordered_gen())


class _Diagram(_Diagram_Global, _Diagram_QOL, metaclass=AutoInitBases):
    """ Core methods of a Diagram. """
    def __init__(self, _single_parent):
        self._single_parent = _single_parent

        self._children = []  # type: list[_Diagram]
        self._parents = []  # type: list[_Diagram]

    @_deco_depth
    def get_children_gen(self, depth=None):
        for child in self._children:
            yield child

    @_deco_depth
    def get_parents_gen(self, depth=None):
        for parent in self._parents:
            yield parent

    @_deco_depth
    def get_nodes_gen(self, depth=None):
        yield from chain(self.get_parents_gen(depth=depth), self.get_children_gen(depth=depth))

    @_deco_cast_to_diagram
    def set_parent(self, parent):
        if self._single_parent or parent is None:
            for old_parent in self._parents:
                old_parent._children.remove(self)
            self._parents.clear()

        elif parent in self._parents:
            parent._children.remove(self)
            self._parents.remove(parent)

        if parent is not None:
            self._parents.append(parent)
            parent._children.append(self)
        return parent

    @_deco_cast_to_diagram
    def add(self, child):
        """ Add a node as child, either with one arg being of own type or with args to create a new one.

            :param any child: """
        child.set_parent(parent=self)
        return child

    @_deco_depth
    def get_siblings_gen(self, depth=None):
        yield from self._siblings_and_spouses(self.get_parents_gen.__func__, self.get_children_gen.__func__)

    def _siblings_and_spouses(self, func1, func2):
        for node1 in func1(self):
            for node2 in func2(node1):
                if node2 is not self:
                    yield node2


class NetworkDiagram(_Diagram, _NetworkDiagram_QOL):
    """ A Diagram where each node can have any amount parents. """
    def __init__(self, _single_parent=False):
        pass

    @_deco_depth
    def get_spouses_gen(self, depth=None):
        yield from self._siblings_and_spouses(self.get_children_gen.__func__, self.get_parents_gen.__func__)


class TreeDiagram(_Diagram, _TreeDiagram_QOL):
    """ A Diagram where each node cannot have more than one parent. """
    def __init__(self, _single_parent=True):
        pass




class A(NetworkDiagram):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


a = A(10)
a.add(2).add(3).add(a)

# b = a.add(20)
# c = a.add(21)
# c.set_parent(11).add(22)



for x in a.get_nodes_gen():
    print(x)  # Here ** Figure out how to combine in get_nodes
















