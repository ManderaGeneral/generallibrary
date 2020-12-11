

class _ObjInfoChildren:
    def get_attribute_child(self, name):
        """ Create a single ObjInfo from this instance's attribute name and put as child.

            :param generallibrary.ObjInfo self:
            :param name: Attribute name. """
        return self.ObjInfo(obj=getattr(self.obj, name), parent=self, name=name)

    def generate_attributes(self):
        """ Generate ObjInfo attribute children with filters correlating to ObjInfo's methods.
            Todo: Somehow prevent duplicate children here.

            :param generallibrary.ObjInfo self: """
        return [self.get_attribute_child(name) for name in dir(self.obj)]

    def __iter__(self):
        return self.generate_attributes()




