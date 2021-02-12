
from generallibrary import *
from generalfile import Path

import generallibrary





# single alternative and generator for each method



def _deco_depth(func):
    def _wrapper(node, depth):
        if depth is None:
            depth = 0
        all_nodes = []
        queue1 = [node]
        while queue1:
            queue2 = []
            for result_node in func(queue1[0]):
                if result_node not in all_nodes:
                    if depth != 0:
                        queue2.append(result_node)
                    all_nodes.append(result_node)
                    yield result_node
            del queue1[0]
            if not queue1:
                queue1 = queue2
                depth -= 1
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


class _Diagram_Global:
    """ Core global methods of a Diagram. """
    def get_ordered(self):
        pass

    def get_ordered_flat(self):
        pass


class _Diagram(_Diagram_Global, _Diagram_QOL, metaclass=AutoInitBases):
    """ Core methods of a Diagram. """
    def __init__(self, _single_parent):
        self._single_parent = _single_parent

        self._children = []  # type: list[_Diagram]
        self._parents = []  # type: list[_Diagram]

    @_deco_depth
    def _get_children(self, depth=None):
        for child in self._children:
            yield child

    def get_nodes(self, depth=None):
        pass

    def get_parents(self, depth=None):
        pass

    def get_siblings(self):
        pass



    def get_children(self, depth=None):
        return list(self._get_children(depth=depth))


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

    @_deco_cast_to_diagram
    def add(self, child):
        """ Add a node as child, either with one arg being of own type or with args to create a new one.

            :param any child: """
        child.set_parent(parent=self)
        return child


@initBases
class NetworkDiagram(_Diagram):
    def __init__(self, _single_parent=False):
        pass

    def get_spouses(self):
        pass


@initBases
class TreeDiagram(_Diagram):
    def __init__(self, _single_parent=True):
        pass





# HERE ** Just added AutoInitBases


class A(NetworkDiagram):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


a = A(1)
a.add(2).add(4)
a.add(3)
print(a.get_children())
















