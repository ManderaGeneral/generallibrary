
from generallibrary.object import initBases
from generallibrary.functions import deco_extend
from generallibrary.values import clamp


import pandas


class Route(list):
    """ List of Nodes (NetworkDiagram) in connected order.
        A route ends when it goes into a dead-end or itself.
        A route can go any direction through links depending on given `incoming` and `outgoing` arguments. """
    def get_links(self):
        """ Get a set of all links connecting nodes in Route.

            :rtype: set[Link] """
        return {link for link in set().union(*[node.links for node in self]) if link.base in self and link.target in self}

    def copy(self):
        """ Simple override to return a new copied Route instance. """
        return Route(self)

    def is_circular(self):
        """ Return whether this Route is circular by seeing if the last node exists more than once. """
        return len(self) > 2 and self[-1] in self[:-3:]

    def is_uturn(self):
        """ Return whether this route is a u-turn by seeing if the last node is the third last node. """
        return len(self) > 2 and self[-1] is self[-3]

    def __repr__(self):
        # return f"{type(self).__name__}: {len(self)}x{' ⟲' * self.is_circular()}{' ⮌' * self.is_uturn()}"
        return f"{type(self).__name__}: {super().__repr__()}{' ⟲' * self.is_circular()}{' ⮌' * self.is_uturn()}"


class RouteGrp(list):
    """ List of Routes. """
    def __init__(self, *routes, origin, depth, incoming, outgoing):
        super().__init__(routes)

        self.origin = origin
        self.depth = depth
        self.incoming = incoming
        self.outgoing = outgoing

    def get_nodes(self):
        """ Get a set of all nodes.

            :rtype: set[NetworkDiagram] """
        return set().union(*self)

    def get_links(self):
        """ Get a set of all links.

            :rtype: set[Link] """
        return set().union(*[route.get_links() for route in self])

    def get_active_links(self, node):
        """ Get a list of direct active links to a node using incoming and outgoing.

            :rtype: list[Link] """
        return [link for link in node.links if link.check_direction(node=node, incoming=self.incoming, outgoing=self.outgoing)]

    def get_connected_nodes(self, node):
        """ Get a list of connected nodes from active links. """
        return [link.other_node(node) for link in self.get_active_links(node=node)]


class Link:
    """ A link between two Nodes. """
    def __init__(self, base, target):
        self.base = base  # type: NetworkDiagram
        self.target = target  # type: NetworkDiagram

    def other_node(self, node):
        """ Return the opposite node of given one. """
        return self.base if self.target is node else self.target

    def check_direction(self, node, incoming, outgoing):
        return (incoming and self.target is node) or (outgoing and self.base is node)

    def __str__(self):
        return f"{self.base} -> {self.target}"
    __repr__ = __str__


class _NetworkDiagram_Global:
    """ Methods for NetworkDiagram that disregards origin. """
    def get_nodes_all(self):
        """ Return a set of all connected Nodes.

            :param NetworkDiagram self:
            :rtype: set[NetworkDiagram] or None """
        return self.get_routes().get_nodes()

    def get_ordered(self):
        """ Return an ordered list containing sets of nodes.
            Starts at node(s) without incoming connections and goes along directions of links.

            :param NetworkDiagram self:
            :rtype: list[set[NetworkDiagram]] or None """
        nodes = self.get_nodes_all()
        order = []
        while nodes:
            order.append(set())
            for node in nodes.copy():
                incoming_nodes = node.get_nodes(outgoing=False)
                if not incoming_nodes.intersection(nodes):
                    order[-1].add(node)

            if not order[-1]:
                raise AttributeError(f"Encountered circular links.")

            nodes -= order[-1]
        return order

    def get_ordered_flat(self):
        return [node for nodes in self.get_ordered() for node in nodes]

    def view(self):
        """ :param NetworkDiagram self: """
        for node in self.get_routes().get_nodes():
            print(f"{node} linked to: {list(node.get_nodes(incoming=False))}")



class NetworkDiagram(_NetworkDiagram_Global):
    """ A network diagram node.
        Todo: Tests for NetworkDiagram.
        Todo: Storable NetworkDiagram.
        Todo: Moveable NetworkDiagram.
        Todo: Transform Network to and from Tree if possible.
        Todo: Remove or hide Network route methods. """
    def __init__(self):
        self.links = []  # type: list[Link]

    def get_link(self, node):
        """ Return a Link this Node has outgoing to another given Node or None. """
        for link in set(self.links).intersection(node.links):
            if link.base is self and link.target is node:
                return link
        return None

    def link(self, target):
        """ Link this Node to another unless the link exists, returns Link regardless. """
        link = self.get_link(node=target)
        if link is None:
            link = Link(base=self, target=target)
            self.links.append(link)
            target.links.append(link)
        return link

    def get_links(self, incoming=True, outgoing=True):
        """ Get a set of links by optional direction connected to this Node.

            :rtype: set[Link] """
        return {link for link in self.links if link.check_direction(node=self, incoming=incoming, outgoing=outgoing)}

    def get_nodes(self, incoming=True, outgoing=True):
        """ Get a set of nodes by optional direction connected to this Node.

            :rtype: set[NetworkDiagram] """
        return {link.other_node(node=self) for link in self.get_links(incoming=incoming, outgoing=outgoing)}

    def get_routes(self, depth=-1, incoming=True, outgoing=True, _route=None, _routes=None):
        """ Get a RouteGrp, a list of Route instances, originating from this Node. """
        if _route is None:
            _route = Route()
            _routes = RouteGrp(_route, origin=self, depth=depth, incoming=incoming, outgoing=outgoing)

        _route.append(self)
        if depth == 0 or _route.count(self) > 1:
            return _routes

        _original_route = _route.copy()
        for i, node in enumerate(_routes.get_connected_nodes(node=self)):
            if i == 0:
                new_route = _route
            else:
                new_route = _original_route.copy()
                _routes.append(new_route)
            node.get_routes(depth=depth - 1, incoming=incoming, outgoing=outgoing, _route=new_route, _routes=_routes)
        return _routes



@deco_extend
class KeyInfo(str):
    """ Store extra info on a string for Diagram key value. """
    def __init__(self, key, use_in_repr, unique):
        self.key = key
        self.use_in_repr = use_in_repr
        self.unique = unique


@initBases
class TreeDiagram:
    """ Saveable tree diagram with optional storage.
        Usage: Inherit TreeDiagram and define what keys to store with `data_keys_add()` method.

        Saves class name and has to access it as an attribute when using `load()`.
        Use metaclass generallibrary.HierarchyStorer to easily store inheriters base class.
        Use initBases decorator to automatically call __init_post__.
        Todo: Idea: Make TreeDiagram loadable with a generic list of lists for example. """
    data_keys = []

    def __init__(self, parent=None, children_dicts=None):
        self._children = []
        self.data = {}
        self._parent = None

        self.hook_create_pre()

    def __init_post__(self, parent=None, children_dicts=None):
        """ Do this stuff post to match TreeDiagram().set_parent() behaviour.
            Otherwise new parent hook is called before inheriters' inits.
            @initBases calls this automatically. """
        self.set_parent(parent=parent, old_parent=None)

        if children_dicts:
            for child_dict in children_dicts:
                self.load(child_dict, parent=self)

        self.hook_create_post()

    def hook_create_pre(self): """ Pre-creation hook. """
    def hook_create_post(self): """ Post-creation hook. """
    def hook_remove(self): """ Remove hook. """
    def hook_new_parent(self, parent, old_parent): """ New parent hook. """
    def hook_lose_parent(self, old_parent, parent): """ Lost parent hook. """
    def hook_add_child(self, child): """ New child hook. """
    def hook_lose_child(self, child): """ Lost child hook. """
    def hook_set_attribute(self, key, value, old_value): """ Attribute set hook. """

    @classmethod
    def data_keys_add(cls, key, value, use_in_repr=False, unique=False, store_now=None):
        """ Define what attributes to keep track of automatically in __setattr__.
            Returns value to enable oneliner in __init__.
            Todo: Removable keys. """
        if cls.data_keys is TreeDiagram.data_keys:
            cls.data_keys = []

        keyInfo = KeyInfo(key=key, use_in_repr=use_in_repr, unique=unique)
        if keyInfo not in cls.data_keys:
            cls.data_keys.append(keyInfo)

        if store_now is not None:
            store_now.data[key] = value

        return value

    def _singular_alternatives(self, list_, index):
        try:
            return list_[index]
        except IndexError:
            return None

    def add(self, *args):
        """ Add a node as child. """
        if type(args[0]) == type(self):
            child = args[0]
        else:
            child = type(self)(*args)

        child.set_parent(parent=self)
        return child

    def set_parent(self, parent, old_parent=..., index=None):
        """ Set a new parent for this Node.

            :param TreeDiagram or None parent:
            :param TreeDiagram or None old_parent:
            :param index: """
        if old_parent is ...:
            old_parent = self._parent

        if old_parent:
            old_parent._children.remove(self)

            old_parent.hook_lose_child(child=self)
            self.hook_lose_parent(old_parent=old_parent, parent=parent)

        if parent:
            # Remove possible existing child with matching unique key values
            for keyInfo in self.data_keys:
                if keyInfo.unique:
                    sibling = parent.get_child_by_key_values(**{keyInfo: getattr(self, keyInfo)})
                    if sibling:
                        sibling.remove()

            # if self in parent.all_parents():
            #     raise AttributeError(f"Cannot set {parent} as parent for {self} as it becomes circular. ")
            if index is None:
                parent._children.append(self)
            else:
                parent._children.insert(index, self)

            parent.hook_add_child(self)
            self.hook_new_parent(parent=parent, old_parent=old_parent)

        self._parent = parent
        # return parent
        return self

    def remove(self):
        """ Remove this Node. """
        self.set_parent(None)
        self.hook_remove()

    def get_all_parents(self):
        """ Get a list of all parents recursively.
            Empty list of no parents.

            :rtype: list[TreeDiagram or Any] """
        part = self
        parents = []
        while part := part.get_parent():
            parents.append(part)
        return parents

    def get_parent(self, index=0):
        """ Get this Node's parent.

            :rtype: TreeDiagram or Any """
        if index == 0:
            return self._parent
        else:
            return self._singular_alternatives(self.get_all_parents(), index)

    def get_children(self):
        """ Get a list of all children this Node has, empty list if None.

            :rtype: list[TreeDiagram or Any] """
        return self._children.copy()

    def get_child(self, index=0):
        """ Get a child by index, None if doesn't exist.

            :rtype: TreeDiagram or Any """
        return self._singular_alternatives(self.get_children(), index)

    def get_children_by_key_values(self, **key_values):
        """ Get a list of children that matches all given key values. """
        return [child for child in self.get_children() if all([getattr(child, key) == value for key, value in key_values.items()])]

    def get_child_by_key_values(self, index=0, **key_values):
        """ Get a child that matches all given key values.

            :rtype: TreeDiagram or Any """
        return self._singular_alternatives(self.get_children_by_key_values(**key_values), index)

    def get_all(self, include_self=True):
        """ Return a flat one-dimensional list of all nodes in this Tree.

            :rtype: list[TreeDiagram or any] """
        nodes = []
        temp = [self]
        while temp:
            treeDiagram = temp[0]
            del temp[0]

            if not (treeDiagram is self and not include_self):
                nodes.append(treeDiagram)

            children = treeDiagram.get_children()
            for child in reversed(children):
                temp.insert(0, child)
        return nodes

    def get_siblings(self):
        """ Get a list of all siblings. """
        if self.get_parent() is None:
            return []
        l = self.get_parent().get_children()
        l.remove(self)
        return l

    def _sibling_helper(self, direction):
        if self.get_parent() is None:
            return None
        parent = self.get_parent()
        children = parent.get_children()
        index = children.index(self) + direction
        return children[index] if 0 <= index < len(children) else None

    def get_next_sibling(self):
        """ Return the next sibling or None if this is the last child. """
        return self._sibling_helper(1)

    def get_previous_sibling(self):
        """ Return the previous sibling or None if this is the last child. """
        return self._sibling_helper(-1)

    def get_index(self):
        """ Return index of this node among it's siblings. """
        assert self.get_parent()
        return self.get_parent().get_children().index(self)

    def set_index(self, index):
        """ Move this node among it's siblings. """
        parent = self.get_parent()
        assert parent
        if parent.get_children()[index] is not self:
            self.remove()
            self.set_parent(parent=parent, index=index)

    def save(self):
        """ Recursively save by returning a new dictionary. """
        data = self.data.copy()
        data["children_dicts"] = [child.save() for child in self.get_children()]
        data["class_name"] = self.__class__.__name__  # Maybe put this in init instead
        return data

    @classmethod
    def load(cls, d, parent=None):
        """ Create a new Tree from a dictionary save.

            :rtype: TreeDiagram or Any """
        class_ = cls if cls.__name__ == d["class_name"] else getattr(cls, d["class_name"], globals().get(d["class_name"]))
        if class_ is None:  # Maybe we could search bases as well, giving us a fourt option... Very messy
            raise AttributeError(f"Couldn't find class '{d['class_name']}' inside itself, try HierarchyStorer.")

        instance = class_(parent=parent, **d)
        # If a key is not already defined by argument in an __init__ (through **d above) then we need to set it here
        for keyInfo in instance.data_keys:
            if getattr(instance, keyInfo, None) != d[keyInfo]:
                setattr(instance, keyInfo, d[keyInfo])
        return instance

    def copy_to(self, parent=None):
        """ Copy this Node along with it's children by using save and load."""
        return self.load(d=self.save(), parent=parent)

    def view(self, indent=1, relative=False, custom_repr=None, spacer=" ", print_out=True):
        """ Get a printable string showing a clear view of this TreeDiagram structure.
            Hides additional lines of a node's repr. """
        top = self.copy_to(None) if relative else self

        lines = []
        for node in top.get_all():
            lanes = []
            all_parents = node.get_all_parents()

            if all_parents:
                del all_parents[-1]
                all_parents.insert(0, node)

            for i, parent in enumerate(all_parents):
                if i == 0:
                    if parent.get_next_sibling():
                        lane = f"├{'─' * indent}{spacer}"
                    else:
                        lane = f"└{'─' * indent}{spacer}"
                else:
                    if parent.get_next_sibling():
                        lane = f"│{spacer * indent}{spacer}"
                    else:
                        lane = f"{spacer}{spacer * indent}{spacer}"

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

    def repr_list(self):
        """ A list of strings used by dunder repr.
            Easily overriden. """
        return [self.data[keyInfo] for keyInfo in self.data_keys if keyInfo.use_in_repr]

    def __repr__(self):
        return f"<{self.__class__.__name__} {', '.join(map(str, self.repr_list()))}>"

        # return f"<{self.__class__.__name__} {repr(getattr(self, '_children', ''))}>"

    def __setattr__(self, key, value):
        if key in self.data_keys:
            old_value = self.data.get(key)
            self.data[key] = value
            self.hook_set_attribute(key=key, value=value, old_value=old_value)
        object.__setattr__(self, key, value)


@initBases
class Markdown(TreeDiagram):
    """ A section for a markdown file, built on TreeDiagram.

        Todo: Create Markdown tree from markdown text.
        Todo: Tests for Markdown.
        Todo: Split line in lines with \n. """
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

    def section_lines(self):
        """ Get a list of all lines in this section. """
        lines = self.lines.copy()
        if self.header:
            lines.insert(0, f"{'#' * clamp(1 + len(self.get_all_parents()), 1, 6)} {self.header}")
        return lines

    def add_lines(self, *lines):
        """ Add lines to list, using splitlines. """
        if self.lines:
            self.lines.append("")

        for line in lines:  # type: str
            self.lines.extend(line.splitlines())
        return self

    def all_lines(self):
        """ Get a list of all lines in this entire Markdown by iterating all children.

            :rtype: list[str] """
        lines = []
        for markdown in self.get_all():
            if lines:
                lines.append("")
            lines.extend(markdown.section_lines())
        return lines

    def add_code_lines(self, *lines):
        """ Add code lines, wrapped by quotes. """
        self.add_lines("```", *lines, "```")
        return self
    
    def add_table_lines(self, *dicts):
        """ Add a table to the lines using pandas `to_markdown`. """
        self.add_lines(pandas.DataFrame(dicts).to_markdown(index=False).replace("_", "\\_"))
        return self
    
    def add_list_lines(self, *items, indent=0):
        """ Add list lines. """
        for item in items:
            self.add_lines(f"{'  ' * indent} - {item}")
        return self

    def add_pre_lines(self, *lines):
        self.add_lines(*lines)
        self.wrap_with_tags("pre")
        return self

    def wrap_with_tags(self, *tags):
        for tag in tags:
            self.lines.insert(0, f"<{tag}>")
            self.lines.append(f"</{tag}>")
        return self

    def __str__(self):
        return '\n'.join(self.all_lines())

