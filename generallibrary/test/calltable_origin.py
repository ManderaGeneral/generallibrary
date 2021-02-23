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



top_objInfo = ObjInfo(Foo())
top_objInfo.filters = []
top_objInfo.get_attrs(depth=1)


callTable = CallTable("ObjInfo").set_args(**{objInfo.name: objInfo for objInfo in top_objInfo.get_all() if objInfo.name})


callTable.generate_with_funcs(
    from_builtin=lambda objInfo: objInfo.from_builtin(),
    from_base=lambda objInfo: objInfo.from_base(),
    from_class=lambda objInfo: objInfo.from_class(),
    from_instance=lambda objInfo: objInfo.from_instance(),
)



