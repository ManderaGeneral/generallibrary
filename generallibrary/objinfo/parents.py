
import sys


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

        if not self.is_module():
            objInfo = None

            # To make the parent of a bound method an instance instead of class
            if dunder_self := getattr(self.obj, "__self__", None):
                objInfo = self.ObjInfo(obj=dunder_self)

            # Start with module and iterate downwards excluding last name in qualname, which we connect manually to self
            elif module and qualname and "<locals>" not in split_qualname:
                objInfo = self.ObjInfo(obj=module)
                for name in split_qualname[:-1:]:
                    objInfo = objInfo.get_attribute_child(name)

            # Find module which contains self.obj
            else:
                first_module, name = next(self._find_modules(), (None, None))
                if first_module:
                    self.name = name
                    objInfo = self.ObjInfo(obj=first_module)

            if objInfo:
                self.set_parent(objInfo)

    def hook_new_parent(self, parent, old_parent):
        """ Assert child is an attribute of it's parent.

            :param generallibrary.ObjInfo self:
            :param parent:
            :param old_parent: """
        assert self.name

        self_obj = self.obj
        parent_attr_obj = getattr(parent.obj, self.name, None)

        if self.is_property():
            self_obj = self_obj.fget
            parent_attr_obj = parent_attr_obj.fget
        else:
            self_obj = getattr(self_obj, "__func__", self_obj)
            parent_attr_obj = getattr(parent_attr_obj, "__func__", parent_attr_obj)

        if parent_attr_obj is not self_obj:
            # print(f"Parent obj {parent.obj}'s '{self.name}' attribute is \n{parent_attr_obj} and not \n{self_obj}")
            raise AssertionError(f"{parent.obj} doesn't seem to have an attribute '{self.name}'.")




