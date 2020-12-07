
from generallibrary.object import initBases

from generallibrary.diagram import TreeDiagram

from generallibrary.objinfo.children import _ObjInfo_children
from generallibrary.objinfo.type import _ObjInfo_type
from generallibrary.objinfo.origin import _ObjInfo_origin
from generallibrary.objinfo.properties import _ObjInfo_properties
from generallibrary.objinfo.parents import _ObjInfo_parents


@initBases
class ObjInfo(_ObjInfo_children, _ObjInfo_type, _ObjInfo_origin, _ObjInfo_properties, _ObjInfo_parents, TreeDiagram):
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





