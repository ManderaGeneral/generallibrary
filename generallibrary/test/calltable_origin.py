""" Generate results from ObjInfo compared with inspect regarding different types of objects.
    Idea is that we could include this automatically in readme or something. """

from generallibrary import ObjInfo, CallTable




class Foo:
    attr = 3
    same = ...

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

Foo.same = Foo

top_objInfo = ObjInfo(Foo())
top_objInfo.get_attrs(depth=-1)

# top_objInfo.view()
# exit()

callTable = CallTable("ObjInfo").set_args(**{objInfo.name: objInfo for objInfo in top_objInfo.get_all() if objInfo.name})

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


callTable.generate_with_funcs(
    from_instance=lambda objInfo: objInfo.from_instance(),
    from_class=lambda objInfo: objInfo.from_class(),
    from_base=lambda objInfo: objInfo.from_base(),
    from_builtin=lambda objInfo: objInfo.from_builtin(),
    from_module=lambda objInfo: objInfo.from_module(),
)



# print(ObjInfo(Foo().a).from_instance())
