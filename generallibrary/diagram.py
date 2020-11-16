
from generallibrary import SigInfo


class TreeDiagram:
    """ Saveable tree diagram with optional storage.
        Inherit TreeDiagram and define what keys to store in `data_keys`.

        Saves class name and has to access it as an attribute when using `load()`.
        Use metaclass generallibrary.HierarchyStorer to easily store inheriters base class.
        Use initBases decorator to automatically call _post_init.
        Todo: TnD """
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

    def hook_create(self): pass
    def hook_remove(self): pass
    def hook_new_parent(self, parent, old_parent): pass
    def hook_lose_parent(self, old_parent, parent): pass
    def hook_add_child(self, child): pass
    def hook_lose_child(self, child): pass
    def hook_set_attribute(self, key, value, old_value): pass

    def _post_init(self):  # @initBases calls this automatically
        self.hook_create()

    def set_parent(self, parent):
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
        return self._parent if index == 0 else self.all_parents()[index]

    def all_parents(self):
        part = self
        parents = []
        while part := part.get_parent():
            parents.append(part)
        return parents

    # Todo: siblings

    def save(self):
        """ Recursively save by returning a new dictionary. """
        data = self.data.copy()
        data["children_dicts"] = [child.save() for child in self.children]
        data["class_name"] = self.__class__.__name__  # Maybe put this in init instead
        return data

    @classmethod
    def load(cls, d, parent=None):
        instance = getattr(cls, d["class_name"])(parent=parent, **d)
        # If a key is not already defined by argument in an __init__ (through **d above) then we need to set it here
        for key in instance.data_keys:
            if getattr(instance, key, None) != d[key]:
                setattr(instance, key, d[key])
        return instance

    def copy_to(self, parent):
        return self.load(d=self.save(), parent=parent)

    def remove(self):
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



from generallibrary.functions import SigInfo