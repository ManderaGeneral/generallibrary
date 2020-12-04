""" Generate results from ObjInfo compared with inspect regarding different types of objects.
    Idea is that we could include this automatically in readme or something. """

from generallibrary import ObjInfo, CallTable


# Parent must have child in it's dir()
# Key comes from __qualname__ or manually set

class Foo:
    _attr = 5
    attr = 3

    def self(self):
        """ Not protected. """
        pass

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



callTable = CallTable("ObjInfo").set_args(**{
    "Foo": Foo,
    "Foo.a": Foo.self,
    "Foo().a": Foo().self,
})


# callTable.generate_with_funcs(
#     from_instance=lambda obj: ObjInfo(obj).from_instance(),
#     from_class=lambda obj: ObjInfo(obj).from_class(),
#     from_base=lambda obj: ObjInfo(obj).from_base(),
#     from_builtin=lambda obj: ObjInfo(obj).from_builtin(),
#     from_module=lambda obj: ObjInfo(obj).from_module(),
# )

# print(ObjInfo(Foo().a).from_instance())
