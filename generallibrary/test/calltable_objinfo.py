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

    bound_cls_method=_Foo()._cls,
    unbound_cls_method=_Foo.__dict__["_cls"],

    bound_static_method=_Foo()._static,
    unbound_static_method=_Foo.__dict__["_static"],

    property=_Foo._property,
)

callTable.args = {key: ObjInfo(value) for key, value in callTable.args.items()}
callTable.name = "ObjInfo"
callTable.generate_with_funcs(**ObjInfo.type_methods)
