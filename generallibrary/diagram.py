

class TreeDiagram:
    """ Saveable tree diagram with optional storage.
        Usage: Inherit TreeDiagram and define what keys to store with `data_keys_add()` method.

        Saves class name and has to access it as an attribute when using `load()`.
        Use metaclass generallibrary.HierarchyStorer to easily store inheriters base class.
        Use initBases decorator to automatically call _post_init.
        Todo: Tests for TreeDiagram. """
    data_keys = []

    def __init__(self, parent=None, children_dicts=None):
        self.children = []
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
        """ Set a new parent for this Node. """
        old_parent = self.get_parent()
        if old_parent:
            old_parent.children.remove(self)

            old_parent.hook_lose_child(child=self)
            self.hook_lose_parent(old_parent=old_parent, parent=parent)

        if parent:
            if self in parent.all_parents():
                raise AttributeError(f"Cannot set {parent} as parent for {self} as it becomes circular. ")
            parent.children.append(self)

            parent.hook_add_child(self)
            self.hook_new_parent(parent=parent, old_parent=old_parent)

        self._parent = parent
        return self

    def get_parent(self, index=0):
        """ Get this Node's parent. """
        return self._parent if index == 0 else self.all_parents()[index]

    def all_parents(self):
        """ Get a list of all parents recursively. """
        part = self
        parents = []
        while part := part.get_parent():
            parents.append(part)
        return parents

    def get_children(self):
        """ Get a list of all children this Node has. """
        return self.children

    # Todo: siblings

    def save(self):
        """ Recursively save by returning a new dictionary. """
        data = self.data.copy()
        data["children_dicts"] = [child.save() for child in self.children]
        data["class_name"] = self.__class__.__name__  # Maybe put this in init instead
        return data

    @classmethod
    def load(cls, d, parent=None):
        """ Create a new Tree from a dictionary save. """
        instance = getattr(cls, d["class_name"])(parent=parent, **d)
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
        return f"<{self.__class__.__name__} {getattr(self, 'children', '')}>"

    def __setattr__(self, key, value):
        if key in self.data_keys:
            old_value = self.data.get(key)
            self.data[key] = value
            self.hook_set_attribute(key=key, value=value, old_value=old_value)
        object.__setattr__(self, key, value)



