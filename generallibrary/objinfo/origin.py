

class _ObjInfoOrigin:
    """ Todo: Finish ObjInfo origins. """
    def from_instance(self):
        """ Get whether this attribute came from the instance.

            :param generallibrary.ObjInfo self: """
        parent = self.get_parent()
        if parent and parent.is_instance():
            return getattr(type(parent.obj), self.name, object()) != self.obj
        else:
            return False


