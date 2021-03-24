
import sys
import importlib


class _ObjInfoParents:
    def spawn_parents(self):
        """ Attempt to generate parents after creation if missing.

            :param generallibrary.ObjInfo self: """
        if self.get_parent(spawn=False) is None:
            module_name = getattr(self.origin, "__module__", None)
            module = sys.modules.get(module_name)

            qualname = getattr(self.origin, "__qualname__", "")
            split_qualname = qualname.split(".")

            objInfo = None
            if self.is_module():
                split_name = self.origin.__name__.split(".")
                for i in range(len(split_name) - 1):
                    parent_module = importlib.import_module(name=".".join(split_name[0:i + 1]))
                    objInfo = self.ObjInfo(obj=parent_module, parent=objInfo)

            else:
                # To make the parent of a bound method an instance instead of class
                if dunder_self := getattr(self.obj, "__self__", None):
                    objInfo = self.ObjInfo(obj=dunder_self)

                # Start with module and iterate downwards excluding last name in qualname, which we connect manually to self
                elif module and qualname and "<locals>" not in split_qualname:
                    objInfo = self.ObjInfo(obj=module)
                    for name in split_qualname[:-1:]:
                        objInfo = self.ObjInfo(obj=getattr(objInfo.obj, name), parent=objInfo, name=name)

                # Find module which contains self.obj
                else:
                    first_module, name = next(self._find_modules(), (None, None))
                    if first_module:
                        # self.name = name  # No idea what this is, but it was strangely breaking test_origins
                        objInfo = self.ObjInfo(obj=first_module)

            if objInfo:
                self.set_parent(objInfo)

    def _find_modules(self):
        """ Get a list of modules that has self.obj as a direct attribute.

            :param generallibrary.ObjInfo self: """
        for module in sys.modules.values():
            for key, value in module.__dict__.items():
                if self.identifier() == self.identifier(obj=value):
                    if self.obj != value:
                        print("Values don't match even though their identifier does.", self.obj, value, self.identifier(), self.identifier(obj=value))
                        # raise AttributeError("Values don't match even though their identifier does.")
                    yield module, key

    @classmethod
    def check_if_parent_eligible(cls, parent_obj, child_obj, name):
        """ Check relationship eligibility of parent to child.

            :param generallibrary.ObjInfo cls:
            :param parent_obj:
            :param child_obj:
            :param name: """

        parent_attr_obj = getattr(parent_obj, name, None)

        parent_attr_obj = cls.get_origin(parent_attr_obj)
        child_obj = cls.get_origin(child_obj)

        if parent_attr_obj is child_obj:
            return True

        return False


