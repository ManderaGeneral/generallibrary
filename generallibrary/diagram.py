
from generallibrary.object import initBases

import pandas


@initBases
class TreeDiagram:
    """ Saveable tree diagram with optional storage.
        Usage: Inherit TreeDiagram and define what keys to store with `data_keys_add()` method.

        Saves class name and has to access it as an attribute when using `load()`.
        Use metaclass generallibrary.HierarchyStorer to easily store inheriters base class.
        Use initBases decorator to automatically call _post_init.
        Todo: Idea: Make TreeDiagram loadable with a generic list of lists for example. """
    data_keys = []

    def __init_subclass__(cls, **kwargs):
        print("there", cls)  # HERE ** Trying to assert that bases uses initBases

    def __init__(self, parent=None, children_dicts=None):
        self._children = []
        self.data = {}
        self.data_keys = []

        self._parent = None
        self.set_parent(parent=parent)

        if children_dicts:
            for child_dict in children_dicts:
                self.load(child_dict, parent=self)

        self.hook_create_pre()

    def hook_create_pre(self): """ Pre-creation hook. """
    def hook_create_post(self): """ Post-creation hook. """
    def hook_remove(self): """ Remove hook. """
    def hook_new_parent(self, parent, old_parent): """ New parent hook. """
    def hook_lose_parent(self, old_parent, parent): """ Lost parent hook. """
    def hook_add_child(self, child): """ New child hook. """
    def hook_lose_child(self, child): """ Lost child hook. """
    def hook_set_attribute(self, key, value, old_value): """ Attribute set hook. """

    def data_keys_add(self, key, value):
        """ Define what attributes to keep track of automatically in __setattr__.
            Returns value to enable oneliner in __init__."""
        self.data_keys.append(key)
        return value

    def _post_init(self):
        """ @initBases calls this automatically. """
        self.hook_create_post()

    def set_parent(self, parent):
        """ Set a new parent for this Node.

            :param TreeDiagram or None parent: """
        old_parent = self.get_parent()
        if old_parent:
            old_parent._children.remove(self)

            old_parent.hook_lose_child(child=self)
            self.hook_lose_parent(old_parent=old_parent, parent=parent)

        if parent:
            if self in parent.all_parents():
                raise AttributeError(f"Cannot set {parent} as parent for {self} as it becomes circular. ")
            parent._children.append(self)

            parent.hook_add_child(self)
            self.hook_new_parent(parent=parent, old_parent=old_parent)

        self._parent = parent
        return self

    def get_parent(self, index=0):
        """ Get this Node's parent.

            :rtype: TreeDiagram """
        try:
            return self._parent if index == 0 else self.all_parents()[index]
        except IndexError:
            return None

    def all_parents(self):
        """ Get a list of all parents recursively.

            :rtype: list[TreeDiagram] """
        part = self
        parents = []
        while part := part.get_parent():
            parents.append(part)
        return parents

    def get_children(self):
        """ Get a list of all children this Node has, empty list if None.

            :rtype: list[TreeDiagram] """
        return self._children.copy()

    def get_child(self, index=0):
        """ Get a child by index, None if doesn't exist. """
        try:
            return self.get_children()[index]
        except IndexError:
            return None

    def get_all(self):
        """ Return a flat one-dimensional list of all nodes in this Tree. """
        l = []
        temp = [self]
        while temp:
            treeDiagram = temp[0]
            del temp[0]

            l.append(treeDiagram)

            children = treeDiagram.get_children()
            for child in reversed(children):
                temp.insert(0, child)
        return l

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

    def save(self):
        """ Recursively save by returning a new dictionary. """
        data = self.data.copy()
        data["children_dicts"] = [child.save() for child in self.get_children()]
        data["class_name"] = self.__class__.__name__  # Maybe put this in init instead
        return data

    @classmethod
    def load(cls, d, parent=None):
        """ Create a new Tree from a dictionary save.

            :rtype: TreeDiagram """
        class_ = cls if cls.__name__ == d["class_name"] else getattr(cls, d["class_name"], globals().get(d["class_name"]))
        if class_ is None:  # Maybe we could search bases as well, giving us a fourt option... Very messy
            raise AttributeError(f"Couldn't find class '{d['class_name']}' inside itself, given dictionary or global scope, try HierarchyStorer.")

        instance = class_(parent=parent, **d)
        # If a key is not already defined by argument in an __init__ (through **d above) then we need to set it here
        for key in instance.data_keys:
            if getattr(instance, key, None) != d[key]:
                setattr(instance, key, d[key])
        return instance

    def copy_to(self, parent=None):
        """ Copy this Node along with it's children by using save and load."""
        return self.load(d=self.save(), parent=parent)

    def remove(self):
        """ Remove this Node. """
        self.set_parent(None)
        self.hook_remove()

    def __repr__(self):
        return f"<{self.__class__.__name__} {repr(getattr(self, '_children', ''))}>"

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
        Todo: Tests for Markdown. """
    def __init__(self, *lines, header=None, hashtags=None, parent=None):
        if hashtags is None:
            hashtags = 2

        self.header = header
        self.lines = list(lines)
        self.hashtags = hashtags

    def section_lines(self):
        """ Get a list of all lines in this section. """
        lines = self.lines.copy()
        if self.header:
            lines.insert(0, f"{'#' * self.hashtags} {self.header}")
        return lines

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
        self.lines.extend(["```", *lines, "```"])
        return self
    
    def add_table_lines(self, list_of_dicts):
        """ Add a table to the lines using pandas `to_markdown`. """
        self.lines.append(pandas.DataFrame(list_of_dicts).to_markdown(index=False))
        return self
    
    def add_list_lines(self, *items, indent=0):
        """ Add list lines. """
        for item in items:
            self.lines.append(f"{'  ' * indent} - {item}")

    def __str__(self):
        return '\n'.join(self.all_lines())

