

class _ObjInfoOrigin:
    def from_instance(self):
        """ Get whether this attribute came from the instance.

            :param generallibrary.ObjInfo self: """
        if parent := self.get_parent():
            return getattr(parent.obj, self.name) != self.obj
        else:
            return False


