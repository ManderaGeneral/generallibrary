

class _ObjInfoProperties:
    def protected(self):
        """ Get whether possible name is protected, False if name is None.

            :param generallibrary.ObjInfo self: """
        return str(self.name).startswith("_")




