

class _ObjInfoChildren:
    """ Set internal state to None to ignore it. """
    children_internal_state = False
    children_builtin_state = False

    all_identifiers = []

    def __init__(self):
        self.spawned_children = False

    def spawn_children(self):
        """ :param generallibrary.ObjInfo self:"""
        if not self.spawned_children:
            self.spawned_children = True

            for name in dir(self.obj):
                if name in ("__dict__", ) or not hasattr(self.obj, name):
                    continue
                attr = getattr(self.obj, name)
                if not self.check_if_parent_eligible(parent_obj=self.obj, child_obj=attr, name=name):
                    continue

                objInfo = self.ObjInfo(obj=attr, name=name)

                if self.children_internal_state is not None and self.children_internal_state != objInfo.internal():
                    continue
                if self.children_builtin_state is not None and self.children_builtin_state != objInfo.from_builtin():
                    continue

                if objInfo.identifier() in self.all_identifiers:
                    objInfo.spawned_children = True  # Include duplicates but don't spawn their children more than once

                self.all_identifiers.append(objInfo.identifier())
                objInfo.set_parent(parent=self)




