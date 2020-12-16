

class _ObjInfoChildren:
    def get_attr(self, name):
        """ Create a single ObjInfo from this instance's attribute name and put as child.

            :param generallibrary.ObjInfo self:
            :param name: Attribute name.
            :rtype: generallibrary.ObjInfo"""
        return self.ObjInfo(obj=getattr(self.obj, name), parent=self, name=name)

    def get_attrs(self, filter_func=None, depth=1):
        """ Get generated attributes as a list.
            Existing attribute ObjInfos will be replaced as the name key is unique.

            :param generallibrary.ObjInfo self:
            :param filter_func: A filter function taking one positional argument ObjInfo.
            :param depth: Depth to iterate, 0 is infinite.
            :rtype: list[generallibrary.ObjInfo] """
        objInfo_list = [] # HERE ** Implement depth
        for name in getattr(self.obj, "__dict__", {}).keys():
            if name in ("__dict__", ):
                continue
            objInfo = self.get_attr(name=name)

            if filter_func is not None and not filter_func(objInfo):
                objInfo.remove()
            else:
                objInfo_list.append(objInfo)
        return objInfo_list

    # def __iter__(self):  # Todo: Define TreeDiagram.__iter__ as well, but without generation.
    #     """ Generate all ObjInfo attribute children.
    #
    #         :param generallibrary.ObjInfo self:
    #         :rtype: collections.Iterable[generallibrary.ObjInfo] """
    #     if hasattr(self.obj, "__dict__"):
    #         for name in self.obj.__dict__.keys():
    #             if name not in ("__dict__", ):
    #                 yield self.get_attribute_child(name=name)




