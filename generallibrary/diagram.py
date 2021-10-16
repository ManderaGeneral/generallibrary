
from generallibrary.functions import AutoInitBases, wrapper_transfer, deco_cast_to_self, Recycle
from generallibrary.values import clamp, confineTo
from generallibrary.iterables import get, pivot_list, subtract_list, flatten



import pandas
from itertools import chain
# import pickle
import dill as pickle  # Can apparently pickle lambdas: https://stackoverflow.com/questions/25348532/can-python-pickle-lambda-functions

def _skip_node_check(node, order_func, filt, traverse_excluded, _all_nodes):
    if node in _all_nodes:
        return True
    if filt and not traverse_excluded and not filt(node):
        return True
    if order_func:
        for order_node in order_func(node):
            if order_node not in _all_nodes:
                return True
    return False


def _traverse(*nodes, func, depth, flat, filt, traverse_excluded, include_self, order_func, vertical, spawn, _all_nodes):
    nodes = [node for node in nodes if not _skip_node_check(node=node, order_func=order_func, filt=filt, traverse_excluded=traverse_excluded, _all_nodes=_all_nodes)]
    if not nodes:
        return StopIteration

    if include_self:
        if filt and traverse_excluded:
            filtered_nodes = [node for node in nodes if filt(node)] if filt else nodes
        else:
            filtered_nodes = nodes

        if flat:
            yield from filtered_nodes
        else:
            yield filtered_nodes
    _all_nodes.extend(nodes)

    if depth is not StopIteration:
        next_depth = StopIteration if depth == 0 else depth - 1
        next_nodes = [node2 for node in nodes for node2 in func(node, spawn=spawn)]

        def next_traverse(*nodes2):
            return _traverse(*nodes2, func=func, depth=next_depth, flat=flat, filt=filt, traverse_excluded=traverse_excluded, include_self=True, order_func=order_func, vertical=vertical, spawn=spawn, _all_nodes=_all_nodes)

        if vertical:
            for node in next_nodes:
                yield from next_traverse(node)

        else:
            yield from next_traverse(*next_nodes)


def _traverser(*nodes, func, depth=None, flat=None, filt=None, traverse_excluded=None, include_self=None, gen=None, vertical=None, order_func=None, spawn=None):
    if depth is None:               depth = 0
    if flat is None:                flat = True
    if traverse_excluded is None:   traverse_excluded = False
    if include_self is None:        include_self = False
    if gen is None:                 gen = False
    if vertical is None:            vertical = True
    if spawn is None:               spawn = True

    generator = _traverse(*nodes, func=func, depth=depth, flat=flat, filt=filt, traverse_excluded=traverse_excluded, include_self=include_self, order_func=order_func, vertical=vertical, spawn=spawn, _all_nodes=[])
    return generator if gen else list(generator)


def _deco_depth(func):
    def _wrapper(node, depth=None, flat=None, filt=None, traverse_excluded=None, include_self=None, gen=None, vertical=None, spawn=None):
        return _traverser(node, func=func, depth=depth, flat=flat, filt=filt, traverse_excluded=traverse_excluded, include_self=include_self, gen=gen, vertical=vertical, spawn=spawn)
    return wrapper_transfer(func, _wrapper)


class _Diagram_QOL:
    """ Quality of life helper methods of Diagram. """
    def _get_children_or_parents(self, parent, child):
        if (parent, child) == (None, None):
            parent = self.get_parent()

        if parent:
            return parent._children
        elif child:
            return child._parents
        else:
            return [self]

    def _singular_alternative(self, method, index, depth, filt, traverse_excluded, include_self, spawn):
        if index is None:
            index = 0
        generator = method.__func__(self, depth=depth, flat=True, gen=True, filt=filt, traverse_excluded=traverse_excluded, include_self=include_self, spawn=spawn)
        if index < 0:
            return get(iterable=tuple(generator), index=index)
        else:
            for i, node in enumerate(generator):
                if i == index:
                    return node

    def get_index(self, parent=None, child=None):
        """ Get the index this node has in target node's container. Parent takes precedence if both are defined.
            Defaults to returning index of first parent's children. Returns 0 if orphan.

            :param TreeDiagram or NetworkDiagram or Any self:
            :param TreeDiagram or NetworkDiagram or Any parent:
            :param TreeDiagram or NetworkDiagram or Any child:
            :raises ValueError: If given node doesn't contain self. """
        return self._get_children_or_parents(parent=parent, child=child).index(self)

    def set_index(self, index, parent=None, child=None):
        """ Set the index this node has in target node's container. Parent takes precedence if both are defined.
            Defaults to setting index of first parent's children. Nothing happens if orphan and parent is defined.

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int index:
            :param TreeDiagram or NetworkDiagram or Any parent:
            :param TreeDiagram or NetworkDiagram or Any child:
            :raises ValueError: If given node doesn't contain self. """
        container = self._get_children_or_parents(parent=parent, child=child)
        if index != container.index(self):
            container.remove(self)
            container.insert(index, self)

    @deco_cast_to_self(if_not_base="_Diagram")
    def add_node(self, child):
        """ Add a node as child, either with one arg being of own type or with args to create a new one.
            Returns child.

            :param TreeDiagram or NetworkDiagram or Any self:
            :param TreeDiagram or NetworkDiagram or Any child: """
        child.set_parent(parent=self)
        return child

    def remove_node(self):
        """ Remove this node recursively. Use set_parent(None) instead if children should be unaffected.

            :param TreeDiagram or NetworkDiagram or Any self: """
        self.set_parent(parent=None)
        if hasattr(self, "recycle_clear"):
            self.recycle_clear()

        for child in self.get_children(gen=True, spawn=False):
            child.remove_node()

    def get_child(self, index=None, depth=None, filt=None, traverse_excluded=None, include_self=None, spawn=None):
        """ Singular QOL alternative for get_children().

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None index: Index of node to be returned. Possible filter is applied before.
            :param int or None depth: Default depth of 0 will return single direct layer. Get unlimited with -1. Previous layers are included.
            :param filt: Optional functional filter, expects 1 node as argument. Applies filter to ALL nodes, including self. See traverse_excluded.
            :param bool or None traverse_excluded: False - Whether to traverse a node even though it has been filtered out from result.
            :param bool or None include_self: False
            :param bool or None spawn: True - Whether to call spawn_* hooks when using get_children or get_parents.
            :rtype: TreeDiagram or NetworkDiagram or Any """
        return self._singular_alternative(self.get_children, index=index, depth=depth, filt=filt, traverse_excluded=traverse_excluded, include_self=include_self, spawn=spawn)

    def get_parent(self, index=None, depth=None, filt=None, traverse_excluded=None, include_self=None, spawn=None):
        """ Singular QOL alternative for get_parents().

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None index: Index of node to be returned. Possible filter is applied before.
            :param int or None depth: Default depth of 0 will return single direct layer. Get unlimited with -1. Previous layers are included.
            :param filt: Optional functional filter, expects 1 node as argument. Applies filter to ALL nodes, including self. See traverse_excluded.
            :param bool or None traverse_excluded: False - Whether to traverse a node even though it has been filtered out from result.
            :param bool or None include_self: False
            :param bool or None spawn: True - Whether to call spawn_* hooks when using get_children or get_parents.
            :rtype: TreeDiagram or NetworkDiagram or Any """
        return self._singular_alternative(self.get_parents, index=index, depth=depth, filt=filt, traverse_excluded=traverse_excluded, include_self=include_self, spawn=spawn)

    def get_node(self, index=None, depth=None, filt=None, traverse_excluded=None, include_self=None, spawn=None):
        """ Singular QOL alternative for get_nodes().

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None index: Index of node to be returned. Possible filter is applied before.
            :param int or None depth: Default depth of 0 will return single direct layer. Get unlimited with -1. Previous layers are included.
            :param filt: Optional functional filter, expects 1 node as argument. Applies filter to ALL nodes, including self. See traverse_excluded.
            :param bool or None traverse_excluded: False - Whether to traverse a node even though it has been filtered out from result.
            :param bool or None include_self: False
            :param bool or None spawn: True - Whether to call spawn_* hooks when using get_children or get_parents.
            :rtype: TreeDiagram or NetworkDiagram or Any """
        return self._singular_alternative(self.get_nodes, index=index, depth=depth, filt=filt, traverse_excluded=traverse_excluded, include_self=include_self, spawn=spawn)

    def get_sibling(self, index=None, depth=None, filt=None, traverse_excluded=None, include_self=None, spawn=None):
        """ Singular QOL alternative for get_siblings().

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None index: Index of node to be returned. Possible filter is applied before.
            :param int or None depth: Default depth of 0 will return single direct layer. Get unlimited with -1. Previous layers are included.
            :param filt: Optional functional filter, expects 1 node as argument. Applies filter to ALL nodes, including self. See traverse_excluded.
            :param bool or None traverse_excluded: False - Whether to traverse a node even though it has been filtered out from result.
            :param bool or None include_self: False
            :param bool or None spawn: True - Whether to call spawn_* hooks when using get_children or get_parents.
            :rtype: TreeDiagram or NetworkDiagram or Any """
        return self._singular_alternative(self.get_siblings, index=index, depth=depth, filt=filt, traverse_excluded=traverse_excluded, include_self=include_self, spawn=spawn)

    def get_ordered_index(self):
        """ Get which layer this node is in based on global get_ordered().

            :param TreeDiagram or NetworkDiagram or Any self: """
        for i, layer in enumerate(self.get_ordered(flat=False, gen=True)):
            if self in layer:
                return i

    def disconnect(self, filt):
        """ Iterate all nodes and set nodes passing the filter's parent to None.

            :param TreeDiagram or NetworkDiagram or Any self:
            :param filt: """
        for node in self.get_all(spawn=False, gen=True, filt=filt, traverse_excluded=True):
            node.set_parent(None)


class _Diagram_Global:
    """ Global methods of a Diagram. """
    def get_all(self, depth=None, flat=None, filt=None, traverse_excluded=None, gen=None, spawn=None):
        """ QOL, shortcut for get_nodes() with depth being -1 and include_self being True.
            Will return/yield all nodes, originating from self.

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None depth: -1 - Depth of 0 will return/yield single direct layer. Get unlimited with -1.
            :param bool or None flat: True - Whether to return/yield nodes directly or in lists. Ignored if vertical.
            :param filt: Optional functional filter, expects 1 node as argument. Applies filter to ALL nodes, including self. See traverse_excluded.
            :param bool or None traverse_excluded: False - Whether to traverse a node even though it has been filtered out from result.
            :param bool or None gen: False - Whether to return a generator or list.
            :param bool or None spawn: True - Whether to call spawn_* hooks when using get_children or get_parents.
            :rtype: list[TreeDiagram or NetworkDiagram or Any] """
        if depth is None:
            depth = -1
        func = self.get_nodes.__func__
        return _traverser(self, func=func, depth=depth, flat=flat, filt=filt, traverse_excluded=traverse_excluded, include_self=True, gen=gen, vertical=True, spawn=spawn)

    def get_ordered(self, depth=None, flat=None, filt=None, traverse_excluded=None, gen=None, spawn=None):
        """ Top to Bottom horizontally.
            Starts with orphan nodes and traverses to return/yield children nodes which have had their respective parents already returned/yielded.

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None depth: -1 - Depth of 0 will return/yield single direct layer. Get unlimited with -1.
            :param bool or None flat: True - Whether to return/yield nodes directly or in lists. Ignored if vertical.
            :param filt: Optional functional filter, expects 1 node as argument. Applies filter to ALL nodes, including self. See traverse_excluded.
            :param bool or None traverse_excluded: False - Whether to traverse a node even though it has been filtered out from result.
            :param bool or None gen: False - Whether to return a generator or list.
            :param bool or None spawn: True - Whether to call spawn_* hooks when using get_children or get_parents.
            :rtype: list[TreeDiagram or NetworkDiagram or Any] """
        if depth is None:
            depth = -1

        origins = [node for node in self.get_all() if not node.get_parents()]
        if not origins:
            raise AttributeError("Could not find any orphan nodes.")
        func = self.get_children.__func__
        order_func = self.get_parents.__func__
        return _traverser(*origins, func=func, depth=depth, flat=flat, filt=filt, traverse_excluded=traverse_excluded, include_self=True, gen=gen, vertical=False, order_func=order_func, spawn=spawn)


class Storable:
    """ Core methods to store, save and load attributes. """
    def save_node(self):
        return pickle.dumps(self)

    @staticmethod
    def load_node(pickled_bytes):
        """ :rtype: TreeDiagram or NetworkDiagram or Any """
        return pickle.loads(pickled_bytes)

    def copy_node(self):
        """ :rtype: TreeDiagram or NetworkDiagram or Any """
        return self.load_node(pickled_bytes=self.save_node())


# class _Diagram_Graph:
#     def __init__(self):
#         self.loops = set()
#
#     def graph(self):
#         """ :param TreeDiagram or NetworkDiagram or Any self: """
#         loops = self.get_loops()
#
#         self._relate_loops(loops=loops)
#         top_loop = loops[0].get_parent(-1, -1, include_self=True)  # type: Loop
#         top_loop.view()
#
#         print(top_loop.available_nodes())  # d shouldn't be available - Maybe try zones instead
#         print(top_loop.unavailable_nodes())
#
#         return loops
#
#     def get_links(self):
#         """ Return a set of sets containing two nodes, paired by child and/or parent.
#
#             :param TreeDiagram or NetworkDiagram or Any self: """
#         links = set()
#         for node in self.get_all():
#             links.update({frozenset({node, child}) for child in node.get_children()})
#             links.update({frozenset({node, parent}) for parent in node.get_parents()})
#         return links
#
#     def get_loops(self):
#         """ Get a list of all unrelated Loops.
#
#             :param TreeDiagram or NetworkDiagram or Any self:
#             :rtype: list[Loop] """
#         loops = self._yield_all_loops()
#         loops = self._exclude_mirrored_loops(loops=loops)
#         loops = self._extract_smallest_loops(loops=loops)
#         self._assign_loops_to_nodes(loops=loops)
#         return loops
#
#     # def _relate_loops(self, loops):
#     #     """ :param TreeDiagram or NetworkDiagram or Any self: """
#     #     related = []
#     #     for loop in loops:
#     #         if not related:
#     #             related.append(loop)
#     #         else:
#     #             for related_loop in related:
#     #                 if related_loop.can_contain(loop=loop):
#     #                     related_loop.add_node(child=loop)
#     #                     break
#     #             else:
#     #                 raise AssertionError("Failed relating loops.")
#
#     def _relate_loops(self, loops):
#         """ Prioritize making top loops parents by iterating children horizontally.
#
#             :param TreeDiagram or NetworkDiagram or Any self: """
#         top = Loop()
#         for loop in loops:
#             for related_loop in top.get_children(depth=-1, include_self=True, vertical=False, gen=True):
#                 if related_loop.can_contain(loop=loop):
#                     related_loop.add_node(child=loop)
#                     break
#             else:
#                 raise AssertionError(f"Failed finding parent for loop {loop}")
#
#     def _extract_smallest_loops(self, loops):
#         """ :param TreeDiagram or NetworkDiagram or Any self: """
#         while True:
#             for loop in loops:
#                 loop_links = loop.get_loop_links()
#                 other_loops = loops.copy()
#                 other_loops.remove(loop)
#
#                 # See if smaller or equal loops have all of the loop_nodes combined
#                 for loop2 in other_loops:
#                     if len(loop2.nodes) <= len(loop.nodes):
#                         loop_links -= loop2.get_loop_links()
#
#                 if not loop_links:
#                     loops.remove(loop)
#                     break
#             else:
#                 break
#
#         return loops
#
#     def _assign_loops_to_nodes(self, loops):
#         """ :param TreeDiagram or NetworkDiagram or Any self: """
#         for node in self.get_all():
#             node.loops.clear()
#         for loop in loops:
#             for node in loop.nodes:
#                 node.loops.add(loop)
#
#     def _exclude_mirrored_loops(self, loops):
#         """ :param TreeDiagram or NetworkDiagram or Any self: """
#         mirrored_loops = []
#         for loop in loops:
#             if not any([loop.equals(old_loop) for old_loop in mirrored_loops]):
#                 mirrored_loops.append(loop)
#         return mirrored_loops
#
#     def _yield_all_loops(self, *nodes):
#         """ :param TreeDiagram or NetworkDiagram or Any self: """
#         nodes = list(nodes) + [self]
#         for node in self.get_nodes():
#             if node in nodes:
#                 if node is not nodes[-2]:
#                     index = nodes.index(node)
#                     yield Loop(*nodes[index:])
#             else:
#                 yield from node._yield_all_loops(*nodes)


class _Diagram(_Diagram_Global, _Diagram_QOL, Storable, metaclass=AutoInitBases):
    """ Core methods of a Diagram. """
    def __init__(self, parent=None):
        # print(hasattr(self, "_children"))
        self._children = []  # type: list[_Diagram]
        self._parents = []  # type: list[_Diagram]

    # def __init_post__(self, parent=None):
        if parent is not None:
            self.set_parent(parent=parent)

    @deco_cast_to_self(if_not_base="_Diagram")
    def set_parent(self, parent):
        """ Set a new parent for this Node.
            Returns parent.

            :param TreeDiagram or NetworkDiagram or Any self:
            :param TreeDiagram or NetworkDiagram or Any parent: """
        if self._single_parent or parent is None:
            for old_parent in self._parents:
                old_parent._children.remove(self)
            self._parents.clear()

        # elif parent in self._parents:
        #     parent._children.remove(self)
        #     self._parents.remove(parent)

        if parent is not None and parent not in self._parents:
            self._parents.append(parent)
            parent._children.append(self)

        return parent

    def spawn_children(self): pass
    def spawn_parents(self): pass

    @_deco_depth
    def get_children(self, depth=None, flat=None, filt=None, traverse_excluded=None, include_self=None, gen=None, vertical=None, spawn=None):
        """ Down.

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None depth: 0 - Depth of 0 will return/yield single direct layer. Get unlimited with -1. Previous layers are included.
            :param bool or None flat: True - Whether to return/yield nodes directly or in lists. Ignored if vertical.
            :param filt: Optional functional filter, expects 1 node as argument. Applies filter to ALL nodes, including self. See traverse_excluded.
            :param bool or None gen: False - Whether to return a generator or list.
            :param bool or None traverse_excluded: False - Whether to traverse a node even though it has been filtered out from result.
            :param bool or None include_self: False
            :param bool or None vertical: True - Whether to traverse one node at a time, or layer by layer.
            :param bool or None spawn: True - Whether to call spawn_* hooks when using get_children or get_parents.
            :rtype: list[TreeDiagram or NetworkDiagram or Any] """
        if spawn:
            self.spawn_children()
        for child in self._children:
            yield child

    @_deco_depth
    def get_parents(self, depth=None, flat=None, filt=None, traverse_excluded=None, include_self=None, gen=None, vertical=None, spawn=None):
        """ Up.

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None depth: 0 - Depth of 0 will return/yield single direct layer. Get unlimited with -1. Previous layers are included.
            :param bool or None flat: True - Whether to return/yield nodes directly or in lists. Ignored if vertical.
            :param filt: Optional functional filter, expects 1 node as argument. Applies filter to ALL nodes, including self. See traverse_excluded.
            :param bool or None gen: False - Whether to return a generator or list.
            :param bool or None traverse_excluded: False - Whether to traverse a node even though it has been filtered out from result.
            :param bool or None include_self: False
            :param bool or None vertical: True - Whether to traverse one node at a time, or layer by layer.
            :param bool or None spawn: True - Whether to call spawn_* hooks when using get_children or get_parents.
            :rtype: list[TreeDiagram or NetworkDiagram or Any] """
        if spawn:
            self.spawn_parents()
        for parent in self._parents:
            yield parent

    @_deco_depth
    def get_nodes(self, depth=None, flat=None, filt=None, traverse_excluded=None, include_self=None, gen=None, vertical=None, spawn=None):
        """ Up + Down.

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None depth: 0 - Depth of 0 will return/yield single direct layer. Get unlimited with -1. Previous layers are included.
            :param bool or None flat: True - Whether to return/yield nodes directly or in lists. Ignored if vertical.
            :param filt: Optional functional filter, expects 1 node as argument. Applies filter to ALL nodes, including self. See traverse_excluded.
            :param bool or None gen: False - Whether to return a generator or list.
            :param bool or None traverse_excluded: False - Whether to traverse a node even though it has been filtered out from result.
            :param bool or None include_self: False
            :param bool or None vertical: True - Whether to traverse one node at a time, or layer by layer.
            :param bool or None spawn: True - Whether to call spawn_* hooks when using get_children or get_parents.
            :rtype: list[TreeDiagram or NetworkDiagram or Any] """
        for node in chain(self.get_parents(gen=True, spawn=spawn), self.get_children(gen=True, spawn=spawn)):
            yield node

    @_deco_depth
    def get_siblings(self, depth=None, flat=None, filt=None, traverse_excluded=None, include_self=None, gen=None, vertical=None, spawn=None):
        """ Up -> Down.

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None depth: 0 - Depth of 0 will return/yield single direct layer. Get unlimited with -1. Previous layers are included.
            :param bool or None flat: True - Whether to return/yield nodes directly or in lists. Ignored if vertical.
            :param filt: Optional functional filter, expects 1 node as argument. Applies filter to ALL nodes, including self. See traverse_excluded.
            :param bool or None gen: False - Whether to return a generator or list.
            :param bool or None traverse_excluded: False - Whether to traverse a node even though it has been filtered out from result.
            :param bool or None include_self: False
            :param bool or None vertical: True - Whether to traverse one node at a time, or layer by layer.
            :param bool or None spawn: True - Whether to call spawn_* hooks when using get_children or get_parents.
            :rtype: list[TreeDiagram or NetworkDiagram or Any] """
        yield from self._siblings_and_spouses(self.get_parents, self.get_children, spawn=spawn)

    def _siblings_and_spouses(self, method1, method2, spawn):
        # for node1 in method1.__func__(self, gen=True, spawn=spawn):
        for node1 in method1.__func__(self, gen=True, spawn=True):
            node_list = method2.__func__(node1, gen=False, spawn=spawn)

            ordered_node_list = pivot_list(list_=node_list, index=node_list.index(self))
            ordered_node_list.remove(self, )

            for node2 in ordered_node_list:
                yield node2


class TreeDiagram(_Diagram):
    """ A Diagram where each node cannot have more than one parent. """
    _single_parent = True

    def __init__(self, parent=None):
        pass

    def view(self, indent=1, relative=False, custom_repr=None, spacer=" ", spawn=False, filt=None, traverse_excluded=False, vertical=True, print_out=True):
        """ Get a printable string showing a clear view of this TreeDiagram structure.
            Hides additional lines of a node's repr. """
        if relative:
            top = self.copy_node()
            top.set_parent(parent=None)
        else:
            top = self

        lines = []
        for node in top.get_children(depth=-1, gen=True, include_self=True, spawn=spawn, filt=filt, traverse_excluded=traverse_excluded, vertical=vertical):
            lanes = []
            all_parents = node.get_parents(depth=-1, spawn=spawn)

            if all_parents:
                del all_parents[-1]
                all_parents.insert(0, node)

            for i, parent in enumerate(all_parents):  # type: int, TreeDiagram
                sibling_index = parent.get_index()
                if i == 0:
                    if len(parent.get_siblings(spawn=spawn)) == sibling_index:
                        lane = f"└{'─' * indent}{spacer}"
                    else:
                        lane = f"├{'─' * indent}{spacer}"
                else:
                    if len(parent.get_siblings(spawn=spawn)) == sibling_index:
                        lane = f"{spacer}{spacer * indent}{spacer}"
                    else:
                        lane = f"│{spacer * indent}{spacer}"

                lanes.insert(0, lane)

            node_str = str(custom_repr(node)) if custom_repr else repr(node)
            if "\n" in node_str:
                node_str = f"{node_str.splitlines()[0]} ..."
            lines.append(f"{''.join(lanes)}{node_str}")

        if relative:
            top.remove_node()

        view = "\n".join(lines)
        if print_out:
            print(view)

        return view


class NetworkDiagram(_Diagram):
    """ A Diagram where each node can have any amount parents. """
    _single_parent = False

    def __init__(self, parent=None):
        pass

    @_deco_depth
    def get_spouses(self, depth=None, flat=None, filt=None, traverse_excluded=None, include_self=None, gen=None, vertical=None, spawn=None):
        """ Down -> Up.

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None depth: 0 - Depth of 0 will return/yield single direct layer. Get unlimited with -1. Previous layers are included.
            :param bool or None flat: True - Whether to return/yield nodes directly or in lists. Ignored if vertical.
            :param filt: Optional functional filter, expects 1 node as argument. Applies filter to ALL nodes, including self. See traverse_excluded.
            :param bool or None gen: False - Whether to return a generator or list.
            :param bool or None traverse_excluded: False - Whether to traverse a node even though it has been filtered out from result.
            :param bool or None include_self: False
            :param bool or None vertical: True - Whether to traverse one node at a time, or layer by layer.
            :param bool or None spawn: True - Whether to call spawn_* hooks when using get_children or get_parents.
            :rtype: list[TreeDiagram or NetworkDiagram or Any] """
        yield from self._siblings_and_spouses(self.get_children, self.get_parents, spawn=spawn)

    def get_spouse(self, index=None, depth=None, filt=None, traverse_excluded=None, include_self=None, spawn=None):
        """ Singular QOL alternative for get_spouses().

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None index: Index of node to be returned. Possible filter is applied before.
            :param int or None depth: Default depth of 0 will return single direct layer. Get unlimited with -1. Previous layers are included.
            :param filt: Optional functional filter, expects 1 node as argument. Applies filter to ALL nodes, including self. See traverse_excluded.
            :param bool or None traverse_excluded: False - Whether to traverse a node even though it has been filtered out from result.
            :param bool or None include_self: False
            :param bool or None spawn: True - Whether to call spawn_* hooks when using get_children or get_parents.
            :rtype: TreeDiagram or NetworkDiagram or Any """
        return self._singular_alternative(self.get_spouses, index=index, depth=depth, filt=filt, traverse_excluded=traverse_excluded, include_self=include_self, spawn=spawn)






class Markdown(TreeDiagram):
    """ A section for a markdown file, built on TreeDiagram. """
    def __init__(self, *lines, header=None, parent=None):
        self.header = header
        self.lines = []
        self.add_lines(*lines)

    def __str__(self):
        return '\n'.join(self.get_all_lines())

    def __contains__(self, item):
        return str(self).__contains__(item)

    @staticmethod
    def link(text, header=None, url=None, href=False, enabled=True):
        """ Return a link to a header or url.
            Enable `href` if inside a non-formatting tag such as <pre>. """
        if not enabled:
            return text
        if url is not None:
            link = url
        else:
            if header is None:
                header = text
            link = f"#{str(header).replace(' ', '-').replace(':', '')}"

        if href:
            return f"<a href='{link}'>{text}</a>"
        return f"[{text}]({link})"

    def get_section_lines(self):
        """ Get a list of all lines in this section. """
        lines = self.lines.copy()
        if self.header:
            lines.insert(0, f"{'#' * clamp(1 + len(self.get_parents(depth=-1)), 1, 6)} {self.header}")
        return lines

    def add_lines(self, *lines):
        """ Add lines to list, using splitlines. """
        for line in lines:  # type: str
            self.lines.extend(str(line).splitlines())
        return self

    def get_all_lines(self):
        """ Get a list of all lines in this entire Markdown by iterating all children.

            :rtype: list[str] """
        lines = []
        for markdown in self.get_all():
            if lines:
                lines.append("")
            lines.extend(markdown.get_section_lines())
        return lines

    def add_table_lines(self, *dicts, sort_by=None):
        """ Add a table to the lines with packed dicts using pandas `to_markdown`. """
        df = pandas.DataFrame(dicts)
        if sort_by is not None:
            df = df.sort_values(by=sort_by)

        self.add_lines(df.to_markdown(index=False))
        return self
    
    def add_list_lines(self, *items, indent=0):
        """ Add list lines. """
        self.add_lines(*[f"{'  ' * indent} - {item}" for item in items])
        return self
    
    def add_code_lines(self, *lines):
        """ Add code lines, wrapped by quotes. """
        self.add_lines(*lines)
        self.wrap_with_tags("```")
        return self

    def add_pre_lines(self, *lines):
        self.add_lines(*lines)
        self.wrap_with_tags("pre")
        return self

    def wrap_with_tags(self, *tags):
        non_tags = "```",
        for tag in tags:
            if tag in non_tags:
                self.lines.insert(0, tag)
                self.lines.append(tag)
            else:
                self.lines.insert(0, f"<{tag}>")
                self.lines.append(f"</{tag}>")
        return self


class Loop(TreeDiagram):
    def __init__(self, *nodes):
        self.nodes = list(nodes)

    def __repr__(self):
        return f"Loop: {self.nodes}"

    def get_loop_links(self):
        return {frozenset({node, self.next_node(node=node)}) for node in self.nodes}

    @property
    def nodes_set(self):
        return set(self.nodes)

    def _next_prev_node(self, node, incr):
        index = confineTo(value=self.nodes.index(node) + incr, minimum=0, maximum=len(self.nodes) - 1, margin=0.5)
        return self.nodes[index]

    def next_node(self, node):
        return self._next_prev_node(node=node, incr=1)

    def prev_node(self, node):
        return self._next_prev_node(node=node, incr=-1)

    def nearby_nodes(self, node):
        return self.next_node(node=node), self.prev_node(node=node)

    def all_nodes(self):
        return set.union(*[loop.nodes_set for loop in self.get_all(gen=True)])

    def equals(self, loop):
        return len(self.nodes) == len(loop.nodes) and not (self.nodes_set - loop.nodes_set)
        # return len(self.nodes) == len(loop.nodes) and not subtract_list(self.nodes, loop.nodes)

    def get_connected_loops(self):
        loops = set.union(*[node.loops for node in self.nodes])
        loops.remove(self)
        return loops

    def get_shared_nodes(self, loop):
        """ Symmetrical. """
        return self.nodes_set.intersection(loop.nodes_set)

    def get_exclusive_nodes(self, loop):
        """ Not symmetrical. """
        return self.nodes_set - self.get_shared_nodes(loop=loop)

    def get_edge_nodes(self, loop):
        """ Symmetrical. """
        exclusive = self.get_exclusive_nodes(loop=loop)  # Could be possible that there are 0 exclusive nodes
        return set(flatten(map(self.nearby_nodes, exclusive))) - exclusive

    # --- Folding logic below ---

    def get_blocked_nodes(self, loop):
        """ Selfs' nodes that loop is blocking.
            Symmetrical. """
        return self.get_shared_nodes(loop=loop) - self.get_edge_nodes(loop=loop)

    def available_nodes(self):
        """ Set of nodes that are available inside self. """
        nodes = self.nodes_set
        for loop in self.get_children():
            nodes -= self.get_blocked_nodes(loop=loop)
            nodes.update(loop.get_exclusive_nodes(loop=self))
        return nodes

    def unavailable_nodes(self):
        """ Set of nodes that exist but are not available inside self. """
        return self.all_nodes() - self.available_nodes()

    def can_contain(self, loop):
        assert loop.get_parent() is None and loop.get_child() is None

        return not loop.nodes_set.intersection(self.unavailable_nodes())









class Zone:
    def __init__(self, *nodes):
        self.nodes = nodes



