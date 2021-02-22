
from generallibrary.functions import AutoInitBases, wrapper_transfer, deco_extend
from generallibrary.values import clamp
from generallibrary.iterables import get

import pandas
from itertools import chain


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
    def view(self):
        pass


class _Diagram_Global:
    """ Core global methods of a Diagram. """
    def get_ordered(self, depth=None, flat=None, gen=None, filt=None):
        """ Top to Bottom.
            Starts with orphan nodes and traverses to return/yield nodes which have had their parents already returned/yielded.

            :param TreeDiagram or NetworkDiagram self:
            :param int or None depth: Default depth of 0 will return/yield single direct layer. Get unlimited with -1.
            :param bool or None flat: Whether to return/yield nodes directly or in lists.
            :param bool or None gen: Whether to return a generator or list.
            :param filt: Optional functional filter, expects 1 node as argument. """
        origins = [node for node in self.get_nodes(-1) if not node.get_parents()]
        if not origins:
            raise AttributeError("Could not find any orphan nodes.")

        func = self.get_children.__func__

        generator = _traverse_depth(*origins, func=func, depth=depth, flat=flat, filt=filt, include_origins=True)
        return _gen_or_list(gen_obj=generator, return_generator=gen)


class _Diagram_Storage:
    """ Core methods to store, save and load attributes. """
    @classmethod
    def data_keys_add(cls, key, value, use_in_repr=False, unique=False):
        """ Define what attributes to keep track of automatically in __setattr__.
            Returns value to enable oneliner in __init__. """
        if cls.data_keys is TreeDiagram.data_keys:
            cls.data_keys = []

        data_key = DataKey(key=key, use_in_repr=use_in_repr, unique=unique)
        if data_key not in cls.data_keys:
            cls.data_keys.append(data_key)

        return value


class _Diagram(_Diagram_Global, _Diagram_QOL, _Diagram_Storage, metaclass=AutoInitBases):
    """ Core methods of a Diagram. """
    data_keys = []

    def __init__(self, parent=None):
        self._children = []  # type: list[_Diagram]
        self._parents = []  # type: list[_Diagram]

        if parent:
            self.set_parent(parent=parent)

    @_deco_cast_to_diagram
    def set_parent(self, parent):
        """ Set a new parent for this Node.

            :param TreeDiagram or NetworkDiagram self:
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
                    filt = lambda node: getattr(node, data_key) == getattr(self, data_key)
                    for sibling in parent.get_children(filt=filt):
                        sibling.set_parent(None)

            self._parents.append(parent)
            parent._children.append(self)
        return parent

    @_deco_cast_to_diagram
    def add(self, child):
        """ Add a node as child, either with one arg being of own type or with args to create a new one.

            :param TreeDiagram or NetworkDiagram self:
            :param TreeDiagram or NetworkDiagram or Any child: """
        child.set_parent(parent=self)
        return child

    @_deco_depth
    def get_children(self, depth=None, flat=None, gen=None, filt=None):
        """ Down.

            :param TreeDiagram or NetworkDiagram self:
            :param int or None depth: Default depth of 0 will return/yield single direct layer. Get unlimited with -1.
            :param bool or None flat: Whether to return/yield nodes directly or in lists.
            :param bool or None gen: Whether to return a generator or list.
            :param filt: Optional functional filter, expects 1 node as argument. """
        for child in self._children:
            yield child

    @_deco_depth
    def get_parents(self, depth=None, flat=None, gen=None, filt=None):
        """ Up.

            :param TreeDiagram or NetworkDiagram self:
            :param int or None depth: Default depth of 0 will return/yield single direct layer. Get unlimited with -1.
            :param bool or None flat: Whether to return/yield nodes directly or in lists.
            :param bool or None gen: Whether to return a generator or list.
            :param filt: Optional functional filter, expects 1 node as argument. """
        for parent in self._parents:
            yield parent

    @_deco_depth
    def get_nodes(self, depth=None, flat=None, gen=None, filt=None):
        """ Up + Down.

            :param TreeDiagram or NetworkDiagram self:
            :param int or None depth: Default depth of 0 will return/yield single direct layer. Get unlimited with -1.
            :param bool or None flat: Whether to return/yield nodes directly or in lists.
            :param bool or None gen: Whether to return a generator or list.
            :param filt: Optional functional filter, expects 1 node as argument. """
        for node in chain(self._children, self._parents):
            yield node

    @_deco_depth
    def get_siblings(self, depth=None, flat=None, gen=None, filt=None):
        """ Up -> Down.

            :param TreeDiagram or NetworkDiagram self:
            :param int or None depth: Default depth of 0 will return/yield single direct layer. Get unlimited with -1.
            :param bool or None flat: Whether to return/yield nodes directly or in lists.
            :param bool or None gen: Whether to return a generator or list.
            :param filt: Optional functional filter, expects 1 node as argument. """
        yield from self._siblings_and_spouses(self.get_parents.__func__, self.get_children.__func__)

    def _siblings_and_spouses(self, func1, func2):
        for node1 in func1(self):
            for node2 in func2(node1):
                if node2 is not self:
                    yield node2


class NetworkDiagram(_Diagram):
    """ A Diagram where each node can have any amount parents. """
    _single_parent = False

    def __init__(self):
        pass

    @_deco_depth
    def get_spouses(self, depth=None, flat=None, gen=None, filt=None):
        """ Down - Up.

            :param TreeDiagram or NetworkDiagram self:
            :param int or None depth: Default depth of 0 will return/yield single direct layer. Get unlimited with -1.
            :param bool or None flat: Whether to return/yield nodes directly or in lists.
            :param bool or None gen: Whether to return a generator or list.
            :param filt: Optional functional filter, expects 1 node as argument. """
        yield from self._siblings_and_spouses(self.get_children.__func__, self.get_parents.__func__)


class TreeDiagram(_Diagram):
    """ A Diagram where each node cannot have more than one parent. """
    _single_parent = True

    def __init__(self):
        pass

    def get_parent(self, depth=None):
        return get(self.get_parents(depth=depth), depth)







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
        for markdown in self.get_nodes(depth=-1):
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








