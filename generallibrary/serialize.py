
from generallibrary.objinfo.objinfo import ObjInfo
from generallibrary.decorators import SigInfo

import json


def _serialize(obj):
    objInfo = ObjInfo(obj)
    objInfos = objInfo.get_children(filt=ObjInfo.is_instance)
    attr_dict = {o.name: o.obj for o in objInfos}
    attr_dict["_obscure_cls_name"] = objInfo.cls.__name__
    if objInfo.is_class():
        attr_dict["_obscure_is_cls"] = True
    return attr_dict

class _Encoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return json.JSONEncoder.default(self, obj)
        except TypeError:
            return _serialize(obj)

def dumps(obj):
    """ Extended dumps function.
        Puts attributes in a dict along with cls_name.
        Dict key numbers are changed to strings, key cannot be custom object. """
    return json.dumps(obj, cls=_Encoder)

def loads(obj, scope=None):
    """ Extended loads function.
        Supply locals() or globals() containing custom class definitions. """
    def object_hook(obj2):
        if isinstance(obj2, dict):
            attr_dict = obj2
            cls_name = attr_dict.get("_obscure_cls_name", None)
            if cls_name:
                cls = (scope or globals())[cls_name]
                sigInfo = SigInfo(cls, **attr_dict)

                is_cls = "_obscure_is_cls" in attr_dict
                new_obj = cls if is_cls else sigInfo.call()

                # Set all attrs manually that were not included in init
                for key, value in attr_dict.items():
                    if getattr(new_obj, key, object()) is not value:
                        setattr(new_obj, key, value)
                return new_obj
        return obj2
    return json.loads(obj, object_hook=object_hook)
