""" Generate results from ObjInfo compared with inspect regarding different types of objects.
    Idea is that we could include this automatically in readme or something. """

from generallibrary import ObjInfo, CallTable

import sys


class Foo:
    attr = 3

    class Test:
        bar = 4

    def __init__(self):
        self.inst = 5

    def self_(self):
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



print(ObjInfo(Foo).get_attrs(lambda objInfo: not objInfo.private()))


# args = {objInfo.name: objInfo.obj for objInfo in ObjInfo(sys.modules["__main__"]).get_attrs(depth=2) if not objInfo.protected()}

# callTable = CallTable("ObjInfo").set_args(**args)

# callTable = CallTable("ObjInfo").set_args(**{
#     "Foo": Foo,
#     "Foo()": Foo(),
#     "Foo.self": Foo.self,
#     "Foo().self": Foo().self,
#     "Foo.attr": Foo.attr,
#     "Foo().attr": Foo().attr,
#     "Foo._cls": Foo._cls,
#     "Foo()._cls": Foo()._cls,
#     "Foo._static": Foo._static,
#     "Foo()._static": Foo()._static,
#     "Foo._property": Foo._property,
#     "Foo()._property": Foo()._property,
#     "Foo().inst": Foo().inst,
# })


# callTable.generate_with_funcs(
#     from_instance=lambda obj: ObjInfo(obj).from_instance(),
#     from_class=lambda obj: ObjInfo(obj).from_class(),
#     from_base=lambda obj: ObjInfo(obj).from_base(),
#     from_builtin=lambda obj: ObjInfo(obj).from_builtin(),
#     from_module=lambda obj: ObjInfo(obj).from_module(),
# )



# print(ObjInfo(Foo().a).from_instance())
