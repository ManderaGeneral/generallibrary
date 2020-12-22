

class _ObjInfoOrigin:
    """ Only one of these methods starting with 'from_' will return True. """
    def _last_cls_with_name(self):
        """ Get the last of parent's cls that has this name in it.

            :param generallibrary.ObjInfo self: """
        last_cls = None
        parent = self.get_parent()
        if parent:
            classes = [type] if parent.cls.mro is type.mro else parent.cls.mro()
            for cls in classes:
                if not hasattr(cls, self.name):
                    break
                last_cls = cls
        return last_cls

    def from_builtin(self):
        """ Get whether this attribute came from a builtin.

            :param generallibrary.ObjInfo self: """
        return getattr(self._last_cls_with_name(), "__module__", None) == "builtins"

    def from_base(self):
        """ Get whether this attribute came from one of it's cls' non-builtin bases.
            Returns first base or False.

            :param generallibrary.ObjInfo self: """
        last_cls = self._last_cls_with_name()
        return last_cls and last_cls is not getattr(self.get_parent(), "cls", None) and getattr(last_cls, "__module__", None) != "builtins"

    def from_class(self):
        """ Get whether this attribute came directly from it's class.

            :param generallibrary.ObjInfo self: """
        return self._last_cls_with_name() is getattr(self.get_parent(), "cls", None)

    def from_instance(self):
        """ Get whether this attribute came from the instance.

            :param generallibrary.ObjInfo self: """
        parent = self.get_parent()
        return bool(parent and parent.is_instance() and not self._last_cls_with_name())




