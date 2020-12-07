

class _ObjInfo_children:
    def get_attribute_child(self, key):
        """ Create a single ObjInfo from this instance's attribute key and put as child.

            :param generallibrary.ObjInfo self:
            :param key: Attribute key. """
        return self.ObjInfo(obj=getattr(self.obj, key), parent=self, key=key)

    def generate_attributes(self):
        """ Generate ObjInfo attribute children with filters correlating to ObjInfo's methods.
            Todo: Somehow prevent duplicate children here.

            :param generallibrary.ObjInfo self: """
        return [self.get_attribute_child(key) for key in dir(self.obj)]

    def __iter__(self):
        return self.generate_attributes()




