
from generallibrary.functions import AutoInitBases, wrapper_transfer, deco_extend
from generallibrary.values import clamp
from generallibrary.iterables import get, join_with_str, pivot_list

import pandas
from itertools import chain
import pickle


def _traverse_depth(*nodes, func, depth, flat, filt, include_origins=False, _all_nodes=None):
    """ Exhausts each depth's nodes to yield results as list, then recursively yields next depth with previous result.
        Possibly yielded origins (If include_origins is True) are unaffected by optional filt attribute.

        Todo: Generalize _traverse_depth() """
    if depth is None:
        depth = 0
    if _all_nodes is None:
        _all_nodes = []
    if flat is None:
        flat = True

    if include_origins:
        if flat:
            yield from nodes
        else:
            yield list(nodes)
        _all_nodes.extend(nodes)

    results = []
    for node1 in nodes:
        for node2 in func(node1):
            if node2 not in _all_nodes and node2 not in results:
                if filt and not filt(node2):
                    continue

                results.append(node2)
                if flat:
                    yield node2

    if results:
        if not flat:
            yield results

        _all_nodes.extend(results)
        if depth != 0:
            yield from _traverse_depth(*results, func=func, depth=depth - 1, flat=flat, filt=filt, _all_nodes=_all_nodes)


def _gen_or_list(gen_obj, return_generator):
    return gen_obj if return_generator else list(gen_obj)


def _deco_depth(func):
    def _wrapper(node, depth=None, flat=None, gen=None, filt=None):
        generator = _traverse_depth(node, func=func, depth=depth, flat=flat, filt=filt)
        return _gen_or_list(gen_obj=generator, return_generator=gen)
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


@deco_extend
class DataKey(str):
    """ Store extra info on a string for Diagram key value. """
    def __init__(self, key, use_in_repr, unique):
        self.key = key
        self.use_in_repr = use_in_repr
        self.unique = unique


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
    def add(self, child):
        """ Add a node as child, either with one arg being of own type or with args to create a new one.
            Returns child.

            :param TreeDiagram or NetworkDiagram or Any self:
            :param TreeDiagram or NetworkDiagram or Any child: """
        child.set_parent(parent=self)
        return child

    def remove(self):
        """ Remove this node, which is simply setting it's parent to None.

            :param TreeDiagram or NetworkDiagram or Any self: """
        self.set_parent(parent=None)

    def get_child(self, index=None, depth=None, filt=None):
        """ Singular QOL alternative for get_children().

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None index: Index of node to be returned. Possible filter is applied before.
            :param int or None depth: Default depth of 0 will return single direct layer. Get unlimited with -1. Previous layers are included.
            :param filt: Optional functional filter, expects 1 node as argument.
            :rtype: TreeDiagram or NetworkDiagram or Any """
        return self._singular_alternative(self.get_children, index=index, depth=depth, filt=filt)

    def get_parent(self, index=None, depth=None, filt=None):
        """ Singular QOL alternative for get_parents().

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None index: Index of node to be returned. Possible filter is applied before.
            :param int or None depth: Default depth of 0 will return single direct layer. Get unlimited with -1. Previous layers are included.
            :param filt: Optional functional filter, expects 1 node as argument.
            :rtype: TreeDiagram or NetworkDiagram or Any """
        return self._singular_alternative(self.get_parents, index=index, depth=depth, filt=filt)

    def get_node(self, index=None, depth=None, filt=None):
        """ Singular QOL alternative for get_nodes().

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None index: Index of node to be returned. Possible filter is applied before.
            :param int or None depth: Default depth of 0 will return single direct layer. Get unlimited with -1. Previous layers are included.
            :param filt: Optional functional filter, expects 1 node as argument.
            :rtype: TreeDiagram or NetworkDiagram or Any """
        return self._singular_alternative(self.get_nodes, index=index, depth=depth, filt=filt)

    def get_sibling(self, index=None, depth=None, filt=None):
        """ Singular QOL alternative for get_siblings().

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None index: Index of node to be returned. Possible filter is applied before.
            :param int or None depth: Default depth of 0 will return single direct layer. Get unlimited with -1. Previous layers are included.
            :param filt: Optional functional filter, expects 1 node as argument.
            :rtype: TreeDiagram or NetworkDiagram or Any """
        return self._singular_alternative(self.get_siblings, index=index, depth=depth, filt=filt)

    def _singular_alternative(self, method, index, depth, filt):
        if index is None:
            index = 0

        generator = method.__func__(self, depth=depth, flat=True, gen=True, filt=filt)
        if index < 0:
            return get(iterable=tuple(generator), index=index)
        else:
            for i, node in enumerate(generator):
                if i == index:
                    return node


class _Diagram_Global:
    """ Core global methods of a Diagram. """
    def get_all(self, depth=None, flat=None, gen=None, filt=None):
        """ Returns/yields all nodes, starting with self.

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None depth: Default depth of -1.
            :param bool or None flat: Whether to return/yield nodes directly or in lists.
            :param bool or None gen: Whether to return a generator or list.
            :param filt: Optional functional filter, expects 1 node as argument.
            :rtype: list[TreeDiagram or NetworkDiagram] """
        if depth is None:
            depth = -1
        func = self.get_nodes.__func__
        generator = _traverse_depth(self, func=func, depth=depth, flat=flat, filt=filt, include_origins=True)
        return _gen_or_list(gen_obj=generator, return_generator=gen)

    def get_ordered(self, depth=None, flat=None, gen=None, filt=None):
        """ Top to Bottom.
            Starts with orphan nodes and traverses to return/yield nodes which have had their parents already returned/yielded.

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None depth: Default depth of 0 will return/yield single direct layer. Get unlimited with -1. Previous layers are included.
            :param bool or None flat: Whether to return/yield nodes directly or in lists.
            :param bool or None gen: Whether to return a generator or list.
            :param filt: Optional functional filter, expects 1 node as argument.
            :raises AttributeError: If there are no orphan nodes. """
        origins = [node for node in self.get_all() if not node.get_parents()]
        if not origins:
            raise AttributeError("Could not find any orphan nodes.")

        func = self.get_children.__func__
        generator = _traverse_depth(*origins, func=func, depth=depth, flat=flat, filt=filt, include_origins=True)
        return _gen_or_list(gen_obj=generator, return_generator=gen)


class _Diagram_Storage:
    """ Core methods to store, save and load attributes. """
    data_keys = []

    @classmethod
    def data_keys_add(cls, key, value, use_in_repr=False, unique=False):
        """ Define what attributes to be unique and to be used in repr. """
        if cls.data_keys is TreeDiagram.data_keys:
            cls.data_keys = []

        data_key = DataKey(key=key, use_in_repr=use_in_repr, unique=unique)
        if data_key not in cls.data_keys:
            cls.data_keys.append(data_key)

        return value

    def repr_list(self):
        """ A list of strings used by dunder repr. """
        return [getattr(self, data_key) for data_key in self.data_keys if data_key.use_in_repr]

    def __repr__(self):
        return f"<{self.__class__.__name__} {join_with_str(', ', self.repr_list())}>"

    def save(self):
        return pickle.dumps(self)

    @staticmethod
    def load(pickled_bytes):
        return pickle.loads(pickled_bytes)

    def copy(self):
        return self.load(pickled_bytes=self.save())


class _Diagram(_Diagram_Global, _Diagram_QOL, _Diagram_Storage, metaclass=AutoInitBases):
    """ Core methods of a Diagram. """
    def __init__(self, parent=None):
        self._children = []  # type: list[_Diagram]
        self._parents = []  # type: list[_Diagram]

        if parent is not None:
            self.set_parent(parent=parent)

    @_deco_cast_to_diagram
    def set_parent(self, parent):
        """ Set a new parent for this Node.
            Returns self.

            :param TreeDiagram or NetworkDiagram or Any self:
            :param TreeDiagram or NetworkDiagram or Any parent: """
        if self._single_parent or parent is None:
            for old_parent in self._parents:
                old_parent._children.remove(self)
            self._parents.clear()

        elif parent in self._parents:
            parent._children.remove(self)
            self._parents.remove(parent)

        if parent is not None:
            # Remove possible existing child with matching unique key values
            for data_key in self.data_keys:
                if data_key.unique:
                    filt = lambda node: getattr(node, data_key, object()) == getattr(self, data_key, object())
                    for sibling in parent.get_children(filt=filt):
                        sibling.set_parent(None)

            self._parents.append(parent)
            parent._children.append(self)
        return self

    @_deco_depth
    def get_children(self, depth=None, flat=None, gen=None, filt=None):
        """ Down.

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None depth: Default depth of 0 will return/yield single direct layer. Get unlimited with -1. Previous layers are included.
            :param bool or None flat: Whether to return/yield nodes directly or in lists.
            :param bool or None gen: Whether to return a generator or list.
            :param filt: Optional functional filter, expects 1 node as argument.
            :rtype: list[TreeDiagram or NetworkDiagram] """
        for child in self._children:
            yield child

    @_deco_depth
    def get_parents(self, depth=None, flat=None, gen=None, filt=None):
        """ Up.

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None depth: Default depth of 0 will return/yield single direct layer. Get unlimited with -1. Previous layers are included.
            :param bool or None flat: Whether to return/yield nodes directly or in lists.
            :param bool or None gen: Whether to return a generator or list.
            :param filt: Optional functional filter, expects 1 node as argument.
            :rtype: list[TreeDiagram or NetworkDiagram] """
        for parent in self._parents:
            yield parent

    @_deco_depth
    def get_nodes(self, depth=None, flat=None, gen=None, filt=None):
        """ Up + Down.

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None depth: Default depth of 0 will return/yield single direct layer. Get unlimited with -1. Previous layers are included.
            :param bool or None flat: Whether to return/yield nodes directly or in lists.
            :param bool or None gen: Whether to return a generator or list.
            :param filt: Optional functional filter, expects 1 node as argument.
            :rtype: list[TreeDiagram or NetworkDiagram] """
        for node in chain(self._children, self._parents):
            yield node

    @_deco_depth
    def get_siblings(self, depth=None, flat=None, gen=None, filt=None):
        """ Up -> Down.

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None depth: Default depth of 0 will return/yield single direct layer. Get unlimited with -1. Previous layers are included.
            :param bool or None flat: Whether to return/yield nodes directly or in lists.
            :param bool or None gen: Whether to return a generator or list.
            :param filt: Optional functional filter, expects 1 node as argument.
            :rtype: list[TreeDiagram or NetworkDiagram] """
        yield from self._siblings_and_spouses(self.get_parents, self.get_children)

    def _siblings_and_spouses(self, method1, method2):
        for node1 in method1.__func__(self, gen=True):
            node_list = method2.__func__(node1, gen=False)

            ordered_node_list = pivot_list(list_=node_list, index=node_list.index(self))
            ordered_node_list.remove(self)

            for node2 in ordered_node_list:
                yield node2


class TreeDiagram(_Diagram):
    """ A Diagram where each node cannot have more than one parent. """
    _single_parent = True

    def __init__(self, parent=None):
        pass

    def get_parent(self, index=None, depth=None, filt=None):
        """ Override to remove redundant depth, as index and depth are very similiar for TreeDiagram's get_parent.

            :rtype: TreeDiagram or NetworkDiagram or Any """
        return _Diagram.get_parent(self=self, index=index, depth=index, filt=filt)

    def view(self, indent=1, relative=False, custom_repr=None, spacer=" ", print_out=True):
        """ Get a printable string showing a clear view of this TreeDiagram structure.
            Hides additional lines of a node's repr. """
        if relative:
            top = self.copy()
            top.set_parent(parent=None)
        else:
            top = self

        lines = []
        for node in [top] + top.get_children(depth=-1):
            lanes = []
            all_parents = node.get_parents(-1)

            if all_parents:
                del all_parents[-1]
                all_parents.insert(0, node)

            for i, parent in enumerate(all_parents):  # type: int, TreeDiagram
                sibling_index = parent.get_index()
                if i == 0:
                    if len(parent.get_siblings()) == sibling_index:
                        lane = f"└{'─' * indent}{spacer}"
                    else:
                        lane = f"├{'─' * indent}{spacer}"
                else:
                    if len(parent.get_siblings()) == sibling_index:
                        lane = f"{spacer}{spacer * indent}{spacer}"
                    else:
                        lane = f"│{spacer * indent}{spacer}"

                lanes.insert(0, lane)

            node_str = str(custom_repr(node) if custom_repr else node)
            if "\n" in node_str:
                node_str = f"{node_str.splitlines()[0]} ..."
            lines.append(f"{''.join(lanes)}{node_str}")

        if relative:
            top.remove()

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
    def get_spouses(self, depth=None, flat=None, gen=None, filt=None):
        """ Down -> Up.

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None depth: Default depth of 0 will return/yield single direct layer. Get unlimited with -1. Previous layers are included.
            :param bool or None flat: Whether to return/yield nodes directly or in lists.
            :param bool or None gen: Whether to return a generator or list.
            :param filt: Optional functional filter, expects 1 node as argument.
            :rtype: list[TreeDiagram or NetworkDiagram] """
        yield from self._siblings_and_spouses(self.get_children, self.get_parents)

    def get_spouse(self, index=None, depth=None, filt=None):
        """ Singular QOL alternative for get_spouses().

            :param TreeDiagram or NetworkDiagram or Any self:
            :param int or None index: Index of node to be returned. Possible filter is applied before.
            :param int or None depth: Default depth of 0 will return single direct layer. Get unlimited with -1. Previous layers are included.
            :param filt: Optional functional filter, expects 1 node as argument.
            :rtype: TreeDiagram or NetworkDiagram or Any """
        return self._singular_alternative(self.get_spouses, index=index, depth=depth, filt=filt)






class Markdown(TreeDiagram):
    """ A section for a markdown file, built on TreeDiagram. """
    def __init__(self, *lines, header=None, parent=None):
        self.header = header
        self.lines = []
        self.add_lines(*lines)

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
            self.lines.extend(line.splitlines())
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

    def __str__(self):
        return '\n'.join(self.get_all_lines())








