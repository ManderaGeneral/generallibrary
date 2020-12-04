""" Generate results from ObjInfo compared with inspect regarding different types of objects.
    Idea is that we could include this automatically in readme or something. """
from generallibrary import ObjInfo, CallTable
import inspect


class _Foo:
    def _self(self):
        pass

    @classmethod
    def _cls(cls):
        pass

    @staticmethod
    def _static():
        pass

    @property
    def _property(self):
        return


def a():
    def b():
        pass
    return b

callTable = CallTable().set_args(
    module=inspect,
    function=a,
    nested_function=a(),
    cls=_Foo,
    instance=_Foo(),

    bound_self_method=_Foo()._self,
    unbound_self_method=_Foo._self,

    bound_inherited_init_method=_Foo().__init__,
    unbound_inherited_init_method=_Foo.__init__,

    bound_cls_method=_Foo()._cls,
    unbound_cls_method=_Foo.__dict__["_cls"],

    bound_static_method=_Foo()._static,
    unbound_static_method=_Foo.__dict__["_static"],

    property=_Foo._property.fget,
)

# callTable.name = "Testing"
# callTable.generate_with_funcs(
#     has_module=lambda obj: obj.__module__,
#     has_qualname=lambda obj: obj.__qualname__,
# )

callTable.name = "ObjInfo"
callTable.generate_with_funcs(
    is_module=lambda obj: ObjInfo(obj).is_module(),
    is_function=lambda obj: ObjInfo(obj).is_function(),
    is_class=lambda obj: ObjInfo(obj).is_class(),
    is_instance=lambda obj: ObjInfo(obj).is_instance(),
    is_method=lambda obj: ObjInfo(obj).is_method(),
    is_property=lambda obj: ObjInfo(obj).is_property(),
    is_method_bound=lambda obj: ObjInfo(obj).is_method_bound(),
)


# callTable.name = "Inspect"
# callTable.generate_with_funcs(
#     ismodule=lambda obj: inspect.ismodule(obj),
#     isfunction=lambda obj: inspect.isfunction(obj),
#     isclass=lambda obj: inspect.isclass(obj),
#     ismethod=lambda obj: inspect.ismethod(obj),
#     ismethoddescriptor=lambda obj: inspect.ismethoddescriptor(obj),
#     callable=lambda obj: callable(obj),
#     isdatadescriptor=lambda obj: inspect.isdatadescriptor(obj),
# )

# callTable.generate_with_funcs(
#     isfunction=lambda obj: inspect.isfunction(obj),
#     ismethod=lambda obj: inspect.ismethod(obj),
#     ismethoddescriptor=lambda obj: inspect.ismethoddescriptor(obj),
#     callable=lambda obj: callable(obj),
#     isdatadescriptor=lambda obj: inspect.isdatadescriptor(obj),
#
#     has_owner=lambda obj: ObjInfo(obj)._owner,
#     has_self=lambda obj: hasattr(obj, "__self__"),
#     has_name=lambda obj: hasattr(obj, "__name__"),
#     has_qualname=lambda obj: hasattr(obj, "__qualname__"),
#     owner_is_instance=lambda obj: ObjInfo(ObjInfo(obj)._owner).is_instance(),
#
#     equals_owner=lambda obj: ObjInfo(obj)._owner.__dict__.get(obj.__name__) == obj,
#
#     is_method_bound=lambda obj: ObjInfo(obj).is_method_bound(),
# )



