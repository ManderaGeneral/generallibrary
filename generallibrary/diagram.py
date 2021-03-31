
from generallibrary.functions import AutoInitBases, wrapper_transfer
from generallibrary.values import clamp
from generallibrary.iterables import get, pivot_list

import pandas
from itertools import chain
import pickle


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


def _deco_cast_to_diagram(func):
    """ Allows first arg to be same type as self or the args the create a new one.

        Todo: Generalize _deco_cast_to_diagram() """
    def _wrapper(self, *args, **kwargs):
        combined = args + tuple(kwargs.values())
        if combined and (combined[0] is None or type(combined[0]) == type(self)):
            diagram = combined[0]
        else:
            diagram = type(self)(*args, **kwargs)
        return func(self, diagram)
    return wrapper_transfer(func, _wrapper)  # Todo: wrapper_transfer for every deco


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

    @_deco_cast_to_diagram
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
            Todo: Reversed get_ordered going Bottom to Top horizontally?

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


class _Diagram_Storage:
    """ Core methods to store, save and load attributes. """
    def save_node(self):
        return pickle.dumps(self)

    @staticmethod
    def load_node(pickled_bytes):
        return pickle.loads(pickled_bytes)

    def copy_node(self):
        return self.load_node(pickled_bytes=self.save_node())


class _Diagram(_Diagram_Global, _Diagram_QOL, _Diagram_Storage, metaclass=AutoInitBases):
    """ Core methods of a Diagram. """
    def __init__(self, parent=None):
        # print(hasattr(self, "_children"))
        self._children = []  # type: list[_Diagram]
        self._parents = []  # type: list[_Diagram]

    # def __init_post__(self, parent=None):
        if parent is not None:
            self.set_parent(parent=parent)

    @_deco_cast_to_diagram
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
        # return self
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








