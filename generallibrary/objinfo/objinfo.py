from collections import ChainMap
from warnings import warn

from generallibrary.iterables import extend_list_in_dict, split_list
from generallibrary.decorators import deco_cache, wrapper_transfer, SigInfo
from generallibrary.diagram import TreeDiagram
from generallibrary.types import getBaseClasses

from generallibrary.objinfo.children import _ObjInfoChildren
from generallibrary.objinfo.type import _ObjInfoType
from generallibrary.objinfo.origin import _ObjInfoOrigin
from generallibrary.objinfo.properties import _ObjInfoProperties
from generallibrary.objinfo.parents import _ObjInfoParents

from typing import Literal, get_args, get_origin


class ObjInfo(_ObjInfoChildren, _ObjInfoType, _ObjInfoOrigin, _ObjInfoProperties, _ObjInfoParents, TreeDiagram):
    """ Get whether obj is a module, function, class, method, property or variable.
        Automatically generates parents post creation for attributes that are not modules.
        Children are generated manually with `generate_attributes`.

        Todo: Recycle ObjInfo.
        Issue is that it becomes a NetworkDiagram (Sort of already is) """

    # _recycle_keys = {"id": lambda obj: ObjInfo._identifier(obj=obj)}
    children_states = {
        _ObjInfoProperties.public: True,

        _ObjInfoOrigin.from_builtin: False,
        # _ObjInfoOrigin.from_instance: None,
        # _ObjInfoOrigin.from_base: None,
        # _ObjInfoOrigin.from_class: None,

        _ObjInfoType.is_module: False,
        # _ObjInfoType.is_function: None,
        # _ObjInfoType.is_class: None,
        # _ObjInfoType.is_property: None,
        # _ObjInfoType.is_instance: None,
        # _ObjInfoType.is_method: None,
    }

    save_node = load_node = copy_node = NotImplemented

    def __init__(self, obj, parent=None, name=None):
        self.obj = obj

        self.cls = self.obj if self.is_class() else type(self.obj)
        self.origin = self.get_origin(self.obj)

        if name is None:
            name = getattr(self.origin, "__name__", None)
            if self.is_module():
                name = name.split(".")[-1]

        self.name = name


    sentinel = object()

    def identifier(self, obj=sentinel):
        """ Returns an identifier for any object. """
        if obj is self.sentinel:
            obj = self.obj
        return self._identifier(obj=obj)

    @staticmethod
    def _identifier(obj):
        return id(obj)

    def __repr__(self):
        """ Return a nice representation string with capitalized type and name. """
        return f"{self.type(nice_output=True)}: {self.name}"

    ObjInfo = ...


setattr(ObjInfo, "ObjInfo", ObjInfo)


class _Hook:
    def __init__(self, func, after):
        self.func = func
        self.after = after


def hook(callable_, *funcs, owner=None, after=False):
    """ Hook into a callable. Stores funcs in callable's instance, class or even module. """
    objInfo = ObjInfo(callable_)
    if owner is None:
        parent = objInfo.get_parent()
        if parent is None:
            raise AttributeError("Could not resolve owner of callable to hook into. Possibly local function?")
        if parent.is_class():
            warn("hook was used on a method without defining owner, prone to mistake as hook will use first base class as owner.")
        owner = parent.obj

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
        setattr(owner, objInfo.name, _wrapper)

    return owner.hooks[objInfo.name]


def cache_clear(obj):
    for objInfo in ObjInfo(obj).get_children(depth=-1, include_self=True, gen=True, filt=lambda objInfo: hasattr(objInfo.obj, "cache_clear"), traverse_excluded=True):
        objInfo.obj.cache_clear()

sentinel = object()
def get_attrs_from_bases(obj, name, /, include_self=True, include_object=True, include_instance=False, ignore=sentinel):
    """ Get a list of attrs which have the same name from every base. """
    attrs = []
    for base in getBaseClasses(obj, includeSelf=include_self, includeObject=include_object, includeInstance=include_instance):
        attr = getattr(base, name, sentinel)
        if attr is not sentinel and attr not in attrs and (ignore is sentinel or attr != ignore):
            attrs.append(attr)
    return attrs

def call_base_hooks(self, name, kwargs=None):
    """ Call a certain method in each base, ignoring overriding.
        Method can take kwargs or nothing as args.
        Kwargs can be updated in each method, returned by this method.
        Note: This function is pretty scuffed, it's very specific for the GUI I think. """
    for base in getBaseClasses(self, includeSelf=True):
        draw_create_hook = getattr(base, name, None)
        if draw_create_hook:
            objInfo = ObjInfo(draw_create_hook, parent=ObjInfo(base))
            if objInfo.defined_by_parent():
                if kwargs is None:
                    draw_create_hook(self)
                else:
                    hook_return = draw_create_hook(self, kwargs=kwargs)
                    if hook_return is not None:
                        kwargs = hook_return
    return kwargs


def dir_appearance_order(obj):
    """ Return list of all attributes as dir does but in the order they appear.
        Maybe this could replace dir() in ObjInfo. """
    __dicts__ = get_attrs_from_bases(obj, "__dict__", include_instance=True)
    return list(ChainMap(*reversed(__dicts__)))

class _DataClass_Class:
    @classmethod
    @deco_cache()
    def _fields_as_objinfos(cls):
        """ Get list of objinfos representing instance attributes sorted by appearance.

            :rtype: list[ObjInfo] """
        def filt(objinfo: ObjInfo):
            return objinfo.is_instance()
        objinfos_by_name = {objinfo.name: objinfo for objinfo in ObjInfo(cls).get_children(traverse_excluded=True, filt=filt)}
        sorted_objinfos = [objinfos_by_name[name] for name in dir_appearance_order(cls) if name in objinfos_by_name]

        return sorted_objinfos

    @classmethod
    @deco_cache()
    def field_keys(cls):
        """ Get a list of field keys defined by subclass.

            :rtype: list[str] """
        return [objinfo.name for objinfo in cls._fields_as_objinfos()]

    @classmethod
    @deco_cache()
    def field_values_defaults(cls):
        """ Get a list of field values defined by subclass.

            :param DataClass cls: """
        return list(cls.field_dict_defaults().values())

    @classmethod
    @deco_cache()
    def field_dict_defaults(cls):
        """ Get a list of field values defined by subclass.

            :param DataClass cls: """
        return {objinfo.name: objinfo.obj for objinfo in cls._fields_as_objinfos()}

    @classmethod
    @deco_cache()
    def field_dict_annotations(cls):
        """ Get a dict of annotations defined by subclass.

            :param DataClass cls: """
        return {key: annotation for key, annotation in getattr(cls, "__annotations__", {}).items() if key in cls.field_keys()}

    @classmethod
    @deco_cache()
    def field_dict_literals(cls):
        """ Get a dict of the annotation Literals as lists.

            :param DataClass cls: """
        return {key: list(get_args(annotation)) for key, annotation in cls.field_dict_annotations().items() if get_origin(annotation) is Literal}



class _DataClass_Instance:
    def field_values(self):
        """ Get a list of field values defined by subclass.

            :param DataClass self: """
        return list(self.field_dict().values())

    def field_dict(self):
        """ Get a dict of the key and values defined by subclass.

            :param DataClass self: """
        return {objinfo.name: getattr(self, objinfo.name) for objinfo in self._fields_as_objinfos()}


class DataClass(_DataClass_Class, _DataClass_Instance):
    pass



