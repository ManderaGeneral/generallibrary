
import sys


class _ObjInfo_parents:
    def hook_create_post(self):
        """ Attempt to generate parents after creation if missing.

            :param generallibrary.ObjInfo self: """
        if self.get_parent() is None:
            self._generate_parents()

    def _generate_parents(self):
        """ Generates all parents to this ObjInfo all the way up to and including module.

            :param generallibrary.ObjInfo self: """
        module_name = getattr(self.obj, "__module__", None)
        module = sys.modules.get(module_name)

        qualname = getattr(self.obj, "__qualname__", "")
        split_qualname = qualname.split(".")

        if module and qualname and "<locals>" not in split_qualname:
            objInfo = self.ObjInfo(obj=module)
            for name in split_qualname[:-1:]:
                objInfo = objInfo.get_attribute_child(name)

            self.set_parent(objInfo)

    def hook_new_parent(self, parent, old_parent):
        """ Assert child is in parent's dir by it's key.

            :param generallibrary.ObjInfo self:
            :param parent:
            :param old_parent: """
        print(self.obj, parent.obj, self.key)
        assert self.key
        assert getattr(parent.obj, self.key, None) is self.obj




