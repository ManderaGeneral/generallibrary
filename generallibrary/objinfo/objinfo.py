
from generallibrary.iterables import extend_list_in_dict, split_list
from generallibrary.functions import SigInfo, wrapper_transfer
from generallibrary.diagram import TreeDiagram

from generallibrary.objinfo.children import _ObjInfoChildren
from generallibrary.objinfo.type import _ObjInfoType
from generallibrary.objinfo.origin import _ObjInfoOrigin
from generallibrary.objinfo.properties import _ObjInfoProperties
from generallibrary.objinfo.parents import _ObjInfoParents


class ObjInfo(_ObjInfoChildren, _ObjInfoType, _ObjInfoOrigin, _ObjInfoProperties, _ObjInfoParents, TreeDiagram):
    """ Get whether obj is a module, function, class, method, property or variable.
        Automatically generates parents post creation for attributes that are not modules.
        Children are generated manually with `generate_attributes`.
        Todo: Disable save, load and copy of ObjInfo's TreeDiagram. """
    def __init__(self, obj, parent=None, name=None):
        self.obj = obj

        self.cls = self.obj if self.is_class() else type(self.obj)
        self.origin = self.get_origin(self.obj)

        if name is None:
            name = getattr(self.origin, "__name__", None)
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


class _Hook:
    def __init__(self, func, after):
        self.func = func
        self.after = after


def hook(callable_, *funcs, after=False):
    """ Hook into a callable. Stores funcs in callable's instance, class or even module. """
    objInfo = ObjInfo(callable_)
    owner = objInfo.get_parent().obj

    if not hasattr(owner, "hooks"):
        owner.hooks = {}
    new = objInfo.name not in owner.hooks
    extend_list_in_dict(owner.hooks, objInfo.name, *[_Hook(func=func, after=after) for func in funcs])

    def _wrapper(*args, **kwargs):
        after, before = split_list(lambda x: x.after, *owner.hooks[objInfo.name])
        sigInfo = SigInfo(callable_, *args, **kwargs)  # Call through SigInfo to easily relay any arguments
        for hook_obj in before:
            sigInfo.call(child_callable=hook_obj.func)
        result = callable_(*args, **kwargs)
        for hook_obj in after:
            sigInfo.call(child_callable=hook_obj.func)
        return result

    if new:
        wrapper_transfer(base=callable_, target=_wrapper)
        setattr(objInfo.get_parent().obj, objInfo.name, _wrapper)

    return owner.hooks[objInfo.name]