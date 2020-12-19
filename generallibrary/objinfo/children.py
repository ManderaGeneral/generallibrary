

class _ObjInfoChildren:
    def get_attrs(self, filter_func=None, depth=1, _all_objInfo=None):
        """ Generate attributes for this ObjInfo's obj.
            Can generate recursively based on depth.
            Existing attribute ObjInfos will be replaced as the name key is unique.
            Returns a list of all generated ObjInfos' identifiers.

            :param generallibrary.ObjInfo self:
            :param filter_func: A filter function taking one positional argument ObjInfo. Defaults to `not objInfo.private()`.
            :param depth: Depth to iterate, -1 is infinite.
            :param _all_objInfo:
            :rtype: list[generallibrary.ObjInfo] """
        if not depth:
            return

        if filter_func is None:
            def filter_func(objInfo):
                """ Default filter. """
                return not objInfo.private()

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

            if filter_func is None or filter_func(objInfo):
                if objInfo.identifier() not in _all_objInfo:
                    objInfo.get_attrs(filter_func=filter_func, depth=depth - 1, _all_objInfo=_all_objInfo)
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




