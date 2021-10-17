""" Generate results from ObjInfo compared with inspect regarding different types of objects.
    Idea is that we could include this automatically in readme or something. """

from generallibrary import ObjInfo, CallTable


class Base:
    base_attr = "hi"

    def base_method(self):
        pass

    def overridden_method(self):
        pass

class Foo(Base):
    attr = 3

    def __init__(self):
        self.inst = 5

    @property
    def _property(self):
        return

    def overridden_method(self):
        pass



callTable = CallTable("ObjInfo").set_args(**{objInfo.name: objInfo for objInfo in ObjInfo(Foo).get_children(depth=1) if objInfo.name})

# callTable = CallTable("ObjInfo").set_args(
#     cls_attr=Foo.attr,
#     cls_base_attr=Foo.base_attr,
#     instance_inst=Foo().inst,
# )


callTable.generate_with_funcs(
    from_builtin=lambda objinfo: objinfo.from_builtin(),
    from_base=lambda objinfo: objinfo.from_base(),
    from_class=lambda objinfo: objinfo.from_class(),
    from_instance=lambda objinfo: objinfo.from_instance(),
    defined_by_parent=lambda objinfo: objinfo.defined_by_parent(),
)



