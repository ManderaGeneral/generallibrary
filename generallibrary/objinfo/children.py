

class _ObjInfoChildren:
    def __init__(self):
        self.filters = [self._default_filter]

    @staticmethod
    def _default_filter(objInfo):
        return not objInfo.internal() and not objInfo.from_builtin()

    def filters_check(self, objInfo):
        """ Check all filter funcs in self.filters.

            :param generallibrary.ObjInfo self:
            :param objInfo: """
        return all([func(objInfo) for func in self.filters])

    def get_attrs(self, depth=1, _all_objInfo=None):
        """ Generate attributes for this ObjInfo's obj.
            Uses self.filters.
            Can generate recursively based on depth.
            Existing attribute ObjInfos will be replaced as the name key is unique.
            Returns a list of all generated ObjInfos' identifiers.

            :param generallibrary.ObjInfo self:
            :param depth: Depth to iterate, -1 is infinite.
            :param _all_objInfo:
            :rtype: list[generallibrary.ObjInfo] """
        if not depth:
            return

        if _all_objInfo is None:
            _all_objInfo = []
        _all_objInfo.append(self.identifier())

        # for name in getattr(self.obj, "__dict__", {}).keys():
        for name in dir(self.obj):
            if name in ("__dict__", ):
                continue

            sentinel = object()
            attr = getattr(self.obj, name, sentinel)
            if attr is sentinel or not self.check_if_parent_eligible(parent_obj=self.obj, child_obj=attr, name=name):
                continue

            objInfo = self.ObjInfo(obj=attr, parent=self, name=name)

            if self.filters_check(objInfo):
                if objInfo.identifier() not in _all_objInfo:
                    objInfo.get_attrs(depth=depth - 1, _all_objInfo=_all_objInfo)
            else:
                objInfo.remove()

        return _all_objInfo

    # def __iter__(self):  # Todo: Define TreeDiagram.__iter__ as well, but without generation.
    #     """ Generate attributes with a depth of 1 and returns a list of direct children.
    #
    #         :param generallibrary.ObjInfo self:
    #         :rtype: collections.Iterable[generallibrary.ObjInfo] """
    #     self.get_attrs()
    #     return self.get_children()




