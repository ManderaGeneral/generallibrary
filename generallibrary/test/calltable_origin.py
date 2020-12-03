""" Generate results from ObjInfo compared with inspect regarding different types of objects.
    Idea is that we could include this automatically in readme or something. """

from generallibrary import ObjInfo, CallTable


class Foo:
    def a(self):
        pass


callTable = CallTable("ObjInfo").set_args(**{
    "Foo": Foo,
    "Foo.a": Foo.a,
    "Foo().a": Foo().a,
})

callTable.generate_with_funcs(
    from_instance=lambda obj: ObjInfo(obj).from_instance(),
    from_class=lambda obj: ObjInfo(obj).from_class(),
    from_base=lambda obj: ObjInfo(obj).from_base(),
    from_builtin=lambda obj: ObjInfo(obj).from_builtin(),
    from_module=lambda obj: ObjInfo(obj).from_module(),
)

print(ObjInfo(Foo().a).from_instance())
