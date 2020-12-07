

class _ObjInfo_properties:
    def protected(self):
        """ Get whether possible key is protected, False if key is None.

            :param generallibrary.ObjInfo self: """
        return str(self.key).startswith("_")




