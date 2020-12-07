
import inspect
from types import MethodWrapperType


class _ObjInfo_type:
    """ Only one of these methods will return True. """
    def is_module(self):
        """ Get whether obj is a module.

            :param generallibrary.ObjInfo self: """
        return inspect.ismodule(self.obj)

    def is_function(self):
        """ Get whether obj is a function.

            :param generallibrary.ObjInfo self: """
        return inspect.isfunction(self.obj) and not self.is_method()

    def is_class(self):
        """ Get whether obj is a class.

            :param generallibrary.ObjInfo self: """
        return inspect.isclass(self.obj)

    def is_property(self):
        """ Get whether obj is a property of a class.

                :param generallibrary.ObjInfo self: """
        return inspect.isdatadescriptor(self.obj)

    def is_instance(self):
        """ Get whether obj is an instance of it's class.

            :param generallibrary.ObjInfo self: """
        return not hasattr(self.obj, "__name__") and not self.is_property() and not self.is_method()

    def is_method(self):
        """ Get whether obj is a method.

            :param generallibrary.ObjInfo self: """
        if inspect.ismethod(self.obj) or inspect.ismethoddescriptor(self.obj):
            return True

        if not callable(self.obj):  # Unbound cls and static methods aren't "callable"
            return False

        if isinstance(self.obj, MethodWrapperType):
            return True

        if parent := self.get_parent():
            if parent.is_class():
                return True

        return False


