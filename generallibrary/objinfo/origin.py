

class _ObjInfoOrigin:
    """ Only one of these methods starting with 'from_' will return True. """
    @staticmethod
    def _cls_has_name(cls, name):
        sentinel = object()
        return getattr(cls, name, sentinel) is not sentinel

    def from_builtin(self):
        """ Get whether this attribute came from a builtin.

            :param generallibrary.ObjInfo self: """
        # parent = self.get_parent()
        # return bool(parent and parent.cls.__module__ == "builtins")
        return bool(self.cls.__module__ == "builtins")

    def from_base(self):
        """ Get whether this attribute came from one of it's bases.
            Returns first base or False.w

            :param generallibrary.ObjInfo self: """
        if self.from_builtin():
            return False

        parent = self.get_parent()
        if parent:
            for base in parent.cls.__bases__:
                if self._cls_has_name(cls=base, name=self.name):
                    return base
        return False

    def from_class(self):
        """ Get whether this attribute came directly from it's class.

            :param generallibrary.ObjInfo self: """
        if self.from_base() or self.from_builtin():
            return False

        parent = self.get_parent()
        return bool(parent and self._cls_has_name(cls=parent.cls, name=self.name))

    def from_instance(self):
        """ Get whether this attribute came from the instance.

            :param generallibrary.ObjInfo self: """
        parent = self.get_parent()
        return bool(parent and parent.is_instance() and not self._cls_has_name(cls=parent.cls, name=self.name))




