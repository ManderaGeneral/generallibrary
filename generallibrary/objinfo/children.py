

class _ObjInfoChildren:
    def get_attribute_child(self, name):
        """ Create a single ObjInfo from this instance's attribute name and put as child.

            :param generallibrary.ObjInfo self:
            :param name: Attribute name. """
        return self.ObjInfo(obj=getattr(self.obj, name), parent=self, name=name)

    def generate_attributes(self):
        """ Get generated attributes as a list.

            :param generallibrary.ObjInfo self: """
        return list(iter(self))

    def __iter__(self):  # Todo: Define TreeDiagram.__iter__ as well, but without generation.
        """ Generate all ObjInfo attribute children.

            :param generallibrary.ObjInfo self: """
        for name in self.obj.__dict__.keys():
            if name not in ("__dict__", ):
                yield self.get_attribute_child(name=name)

        # return iter(self.generate_attributes())




