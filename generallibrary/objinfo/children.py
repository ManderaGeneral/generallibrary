

class _ObjInfoChildren:
    def get_attr(self, name):
        """ Create a single ObjInfo from this instance's attribute name and put as child.

            :param generallibrary.ObjInfo self:
            :param name: Attribute name.
            :rtype: generallibrary.ObjInfo"""
        return self.ObjInfo(obj=getattr(self.obj, name), parent=self, name=name)

    def get_attrs(self, filter_func=None, depth=1):
        """ Generate attributes for this ObjInfo's obj.
            Can generate recursively based on depth.
            Existing attribute ObjInfos will be replaced as the name key is unique.
            Returns a list of all recursive children.

            :param generallibrary.ObjInfo self:
            :param filter_func: A filter function taking one positional argument ObjInfo.
            :param depth: Depth to iterate, -1 is infinite.
            :rtype: list[generallibrary.ObjInfo]
            Todo: Infinite loop prevention for get_attrs(). """
        for name in getattr(self.obj, "__dict__", {}).keys():
            if name in ("__dict__", ):
                continue
            objInfo = self.get_attr(name=name)

            if filter_func is not None and not filter_func(objInfo):
                objInfo.remove()
            else:
                if depth != 0:
                    objInfo.get_attrs(filter_func=filter_func, depth=depth - 1)

        return self.get_all()

    def __iter__(self):  # Todo: Define TreeDiagram.__iter__ as well, but without generation.
        """ Generate attributes with a depth of 1 and returns a list of direct children.

            :param generallibrary.ObjInfo self:
            :rtype: collections.Iterable[generallibrary.ObjInfo] """
        self.get_attrs()
        return self.get_children()




