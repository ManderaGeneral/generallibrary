

class _ObjInfoOrigin:
    """ Todo: Finish ObjInfo origins. """
    def from_instance(self):
        """ Get whether this attribute came from the instance.

            :param generallibrary.ObjInfo self: """
        parent = self.get_parent()
        if parent and parent.is_instance():
            return getattr(type(parent.obj), self.name, object()) != self.obj
        return False

    def from_class(self):
        """ Get whether this attribute came from it's class.

            :param generallibrary.ObjInfo self: """
        parent = self.get_parent()
        if parent and parent.is_class():
            return getattr(parent.obj, self.name, object()) == self.obj
        return False



