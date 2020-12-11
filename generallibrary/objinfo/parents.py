
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
            except (ValueError, TypeError):
                module_has_obj = False

            if module_has_obj:
                for key, value in module.__dict__.items():
                    if value == self.obj:
                        yield module, key

    def _generate_parents(self):
        """ Generates all parents to this ObjInfo all the way up to and including module.

            :param generallibrary.ObjInfo self: """
        module_name = getattr(self.obj, "__module__", None)
        module = sys.modules.get(module_name)

        qualname = getattr(self.obj, "__qualname__", "")
        split_qualname = qualname.split(".")

        if not self.is_module():
            # Start with module and iterate downwards excluding last name in qualname, which we connect manually to self
            if module and qualname and "<locals>" not in split_qualname:
                objInfo = self.ObjInfo(obj=module)
                for name in split_qualname[:-1:]:
                    objInfo = objInfo.get_attribute_child(name)
                self.set_parent(objInfo)

            else:
                first_module, name = next(self._find_modules(), (None, None))
                if first_module:
                    self.name = name
                    self.set_parent(self.ObjInfo(obj=first_module))

    def hook_new_parent(self, parent, old_parent):
        """ Assert child is in parent's dir by it's name.

            :param generallibrary.ObjInfo self:
            :param parent:
            :param old_parent: """
        assert self.name
        if getattr(parent.obj, self.name, None) is not self.obj:
            raise AssertionError(f"Parent obj {parent.obj}'s '{self.name}' attribute name is \n{getattr(parent.obj, self.name, None)} and not \n{self.obj}")




