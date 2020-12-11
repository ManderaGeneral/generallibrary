

class _ObjInfoChildren:
    def get_attribute_child(self, name):
        """ Create a single ObjInfo from this instance's attribute name and put as child.

            :param generallibrary.ObjInfo self:
            :param name: Attribute name. """
        return self.ObjInfo(obj=getattr(self.obj, name), parent=self, name=name)

    def generate_attributes(self):
        """ Generate all ObjInfo attribute children.

            :param generallibrary.ObjInfo self: """
        return [self.get_attribute_child(name) for name in self.obj.__dict__.keys() if name not in ("__dict__", )]

    def __iter__(self):  # Not sure why I added this. X in ObjInfo? Should we have this in TreeDiagram?
        return self.generate_attributes()




