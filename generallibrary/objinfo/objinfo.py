
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
        Todo: Another type of diagram for ObjInfo as an object can be an attribute of multiple objects. """
    def __init__(self, obj, parent=None, name=None):
        self.obj = obj

        if name is None:
            if self.is_property():
                name = self.obj.fget.__name__
            else:
                name = getattr(self.obj, "__name__", None)

        self.name = self.data_keys_add(key="name", value=name, use_in_repr=True, unique=True)

    ObjInfo = ...


setattr(ObjInfo, "ObjInfo", ObjInfo)







