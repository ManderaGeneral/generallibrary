
from generallibrary.object import initBases

from generallibrary.diagram import TreeDiagram

from generallibrary.objinfo.children import _ObjInfoChildren
from generallibrary.objinfo.type import _ObjInfoType
from generallibrary.objinfo.origin import _ObjInfoOrigin
from generallibrary.objinfo.properties import _ObjInfoProperties
from generallibrary.objinfo.parents import _ObjInfoParents


@initBases
class ObjInfo(_ObjInfoChildren, _ObjInfoType, _ObjInfoOrigin, _ObjInfoProperties, _ObjInfoParents, TreeDiagram):
    """ Get whether obj is a module, function, class, method, property or variable.
        Automatically generates parents post creation for attributes that are not modules.
        Children are generated manually with `generate_attributes`.
        Todo: Module tree for ObjInfo.
        Todo: Another type of diagram for ObjInfo as an object can be an attribute of multiple objects.
        Todo: Tests for ObjInfo.
        Todo: Disable save, load and copy. """
    def __init__(self, obj, parent=None, name=None):
        self.obj = obj
        self.cls = self.obj if self.is_class() else type(self.obj)

        if name is None:
            if self.is_property():
                name = self.obj.fget.__name__
            else:
                name = getattr(self.obj, "__name__", None)
                if self.is_module():
                    name = name.split(".")[-1]

        self.name = self.data_keys_add(key="name", value=name, use_in_repr=True, unique=True)  # type: str

    def repr_list(self):
        """ Overried TreeDiagram's repr content to show type. """
        return super().repr_list() + [self.type()]

    def identifier(self):
        """ Returns a tuple of parent's obj's id and it's own's obj's id.
            Made for ObjInfo.get_attrs(), I want to have identical attributes listed, but not it's attributes. """
        return id(self.obj)
        # return id(getattr(self.get_parent(), "obj", None)), id(self.obj)

    def nice_repr(self):
        """ Return a nice represantion string with capitalized type and name. """
        return f"{self.type(nice_output=True)}: {self.name}"

    ObjInfo = ...


setattr(ObjInfo, "ObjInfo", ObjInfo)





