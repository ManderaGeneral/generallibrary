
import inspect


class _ObjInfoOrigin:
    """ Only one of these methods starting with 'from_' will return True. """
    def _last_cls_with_name(self):
        """ Get the last (bottom-most) of parent's cls that has this name in it.

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
        names = "fget", "fset", "fdel", "denominator", "imag", "numerator", "real", "cache_parameters"
        return inspect.isbuiltin(self.obj) or getattr(self._last_cls_with_name(), "__module__", None) == "builtins" or self.name in names

    def from_base(self):
        """ Get whether this attribute came from one of it's cls' non-builtin bases.
            Returns first base or False.

            :param generallibrary.ObjInfo self: """
        last_cls = self._last_cls_with_name()
        return last_cls and last_cls is not getattr(self.get_parent(), "cls", None) and getattr(last_cls, "__module__", None) != "builtins"

    def from_class(self):
        """ Get whether this attribute came directly from it's class.
            Doesn't matter if direct parent has overridden inherited attr.
            Sees if bottom-most occurrence is direct parent.
            # Subset of from_class_with_overrides.

            :param generallibrary.ObjInfo self: """
        return self._last_cls_with_name() is getattr(self.get_parent(), "cls", None)

    # def from_class_with_overrides(self):  # This would violate only one from_* being True rule
    #     """ Get whether this attribute is defined by it's direct parent, even if a base class has it.
    #
    #         :param generallibrary.ObjInfo self: """
    #     return self._last_cls_with_name() is getattr(self.get_parent(), "cls", None)

    def from_instance(self):
        """ Get whether this attribute came from the instance.

            :param generallibrary.ObjInfo self: """
        parent = self.get_parent()
        return bool(parent and parent.is_instance() and not self._last_cls_with_name())

    def from_module(self):
        """ Get whether this attribute's parent is a module.

            :param generallibrary.ObjInfo self: """
        parent = self.get_parent()
        return bool(parent and parent.is_module())




