""" Todo: Subset methods for ObjInfo.is_method(). """


# def subset_is_method_bound(self):
#     """ Subset of `is_method`: Get whether a method is bound. """
#     assert self.is_method()
#
#     has_self = hasattr(self.obj, "__self__")
#     if has_self:
#         return True
#
#     parent = self.get_parent()
#     if parent:
#         # if parent.obj.__dict__.get(self.obj.__name__) == self.obj:
#         if getattr(parent.obj, self.obj.__name__, None) == self.obj:
#             return False
#
#         if not has_self:
#             return True
#
#     return False

