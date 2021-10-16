""" Generate results from ObjInfo compared with inspect regarding different types of objects.
    Idea is that we could include this automatically in readme or something. """

from generallibrary import ObjInfo, CallTable


class Base:
    base_attr = "hi"

class Foo(Base):
    attr = 3

    def __init__(self):
        self.inst = 5

    @property
    def _property(self):
        return



# callTable = CallTable("ObjInfo").set_args(**{objInfo.name: objInfo for objInfo in ObjInfo(Foo()).get_all(depth=1) if objInfo.name})

callTable = CallTable("ObjInfo").set_args(
    cls_attr=Foo.attr,
    cls_base_attr=Foo.base_attr,
    instance_inst=Foo().inst,
)


callTable.generate_with_funcs(
    from_builtin=lambda attr: ObjInfo(attr).from_builtin(),
    from_base=lambda attr: ObjInfo(attr).from_base(),
    from_class=lambda attr: ObjInfo(attr).from_class(),
    from_instance=lambda attr: ObjInfo(attr).from_instance(),
)



