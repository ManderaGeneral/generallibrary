
import generallibrary
# import generalvector
# import generalfile
# import generalgui
# generallibrary.attributes_to_markdown(generallibrary)
# generallibrary.attributes_to_markdown(generalvector)
# generallibrary.attributes_to_markdown(generalfile)
# generallibrary.attributes_to_markdown(generalgui)


from generallibrary import ObjInfo, SigInfo
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


# print(type(_Foo().__init__))
# print(SigInfo(_Foo()._self).class_from_callable())
# print(_Foo._self.__globals__)
# exit()


import pandas as pd

class CallTable:
    def __init__(self, name=None):
        self.name = name

        self.funcs = {}
        self.args = {}

    def set_funcs(self, **funcs):
        """ Set all funcs. """
        self.funcs = funcs
        return self

    def set_args(self, **args):
        """ Set all args. """
        self.args = args
        return self

    def _generate(self, funcs=None, args=None):
        if funcs is None:
            funcs = self.funcs
        if args is None:
            args = self.args

        columns = {}
        for func_name, func in funcs.items():
            # columns[func_name] = {arg_name: func(arg) for arg_name, arg in args.items()}
            columns[func_name] = {arg_name: "True" if func(arg) else "" for arg_name, arg in args.items()}

        df = pd.DataFrame(columns)
        df = df.rename_axis(self.name)

        print(df.to_markdown(), "\n")

    def generate(self):
        """ Generate table with stored funcs and args. """
        return self._generate()

    def generate_with_args(self, **args):
        """ Generate table with stored funcs and new args. """
        return self._generate(args=args)

    def generate_with_funcs(self, **funcs):
        """ Generate table with stored args and new funcs. """
        return self._generate(funcs=funcs)

callTable = CallTable("ObjInfo").set_args(
    module=generallibrary,
    function=a,
    nested_function=a(),
    cls=_Foo,
    instance=_Foo(),

    bound_self_method=_Foo()._self,
    unbound_self_method=_Foo._self,

    bound_init_method=_Foo().__init__,
    unbound_init_method=_Foo.__init__,

    bound_cls_method=_Foo()._cls,
    unbound_cls_method=_Foo._cls,

    bound_static_method=_Foo()._static,
    unbound_static_method=_Foo._static,

    property=_Foo._property,
)

callTable.generate_with_funcs(
    is_module=lambda obj: ObjInfo(obj).is_module(),
    is_function=lambda obj: ObjInfo(obj).is_function(),
    is_class=lambda obj: ObjInfo(obj).is_class(),
    is_instance=lambda obj: ObjInfo(obj).is_instance(),
    is_method=lambda obj: ObjInfo(obj).is_method(),
    is_property=lambda obj: ObjInfo(obj).is_property(),
)


callTable.name = "Inspect"
callTable.generate_with_funcs(
    ismodule=lambda obj: inspect.ismodule(obj),
    isfunction=lambda obj: inspect.isfunction(obj),
    isclass=lambda obj: inspect.isclass(obj),
    ismethod=lambda obj: inspect.ismethod(obj),
    ismethoddescriptor=lambda obj: inspect.ismethoddescriptor(obj),
)

# HERE ** Put CallTable in lib. Keep working on ObjInfo with attrs. Update attributes() to use it.
