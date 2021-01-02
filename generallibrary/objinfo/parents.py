
import sys
import importlib


class _ObjInfoParents:
    def hook_create_post(self):
        """ Attempt to generate parents after creation if missing.

            :param generallibrary.ObjInfo self: """
        if self.get_parent() is None:
            self._generate_parents()

    def _find_modules(self):
        """ Get a list of modules that has self.obj as a direct attribute.

            :param generallibrary.ObjInfo self: """
        for module in sys.modules.values():
            try:
                module_has_obj = self.obj in module.__dict__.values()
            except:
                module_has_obj = False

            if module_has_obj:
                for key, value in module.__dict__.items():
                    if value == self.obj:
                        yield module, key

    def _generate_parents(self):
        """ Generates all parents to this ObjInfo all the way up to and including module.

            :param generallibrary.ObjInfo self: """
        obj = self.obj.fget if self.is_property() else self.obj

        module_name = getattr(obj, "__module__", None)
        module = sys.modules.get(module_name)

        qualname = getattr(obj, "__qualname__", "")
        split_qualname = qualname.split(".")

        objInfo = None
        if self.is_module():
            split_name = self.obj.__name__.split(".")
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
                    self.name = name
                    objInfo = self.ObjInfo(obj=first_module)

        if objInfo:
            self.set_parent(objInfo)

    @classmethod
    def check_if_parent_eligible(cls, parent_obj, child_obj, name):
        """ Check relationship eligibility of parent to child.
            :param generallibrary.ObjInfo cls:
            :param parent_obj:
            :param child_obj:
            :param name: """
        parent_attr_obj = getattr(parent_obj, name, None)

        if cls._is_property(child_obj):
            child_obj = child_obj.fget
            parent_attr_obj = parent_attr_obj.fget
        else:
            child_obj = getattr(child_obj, "__func__", child_obj)
            parent_attr_obj = getattr(parent_attr_obj, "__func__", parent_attr_obj)

        if parent_attr_obj is child_obj:
            return True
        return False

    def hook_new_parent(self, parent, old_parent):
        """ Assert child is an attribute of it's parent.

            :param generallibrary.ObjInfo self:
            :param parent:
            :param old_parent: """
        assert self.name
        assert self.check_if_parent_eligible(parent.obj, self.obj, self.name)




