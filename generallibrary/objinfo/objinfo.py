
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
        Automatically generates parents post creation for attributes.
        Children are generated manually with `generate_attributes`. """
    def __init__(self, obj, parent=None, key=None):
        self.obj = obj

        if key is None:
            key = getattr(self.obj, "__name__", None)
        self.key = self.data_keys_add("key", key, use_in_repr=True)

    ObjInfo = ...


ObjInfo.ObjInfo = ObjInfo





