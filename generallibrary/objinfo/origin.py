

class _ObjInfoOrigin:
    """ Todo: Finish ObjInfo origins. """
    def from_instance(self):
        """ Get whether this attribute came from the instance.

            :param generallibrary.ObjInfo self: """
        parent = self.obj
        if parent and parent.is_instance():
            return getattr(parent.obj, self.name) != self.obj
        else:
            return False


