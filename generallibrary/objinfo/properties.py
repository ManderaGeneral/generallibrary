

class _ObjInfoProperties:
    def internal(self):
        """ Get whether possible name is for internal use, False if name is None.
            True if private or protected.

            :param generallibrary.ObjInfo self: """
        return self.private() or self.protected()

    def private(self):
        """ Get whether possible name is private, False if name is None.
            Subset of ObjInfo.internal().

            :param generallibrary.ObjInfo self: """
        return str(self.name).startswith("__")

    def protected(self):
        """ Get whether possible name is protected, False if name is None.
            Subset of ObjInfo.internal().

            :param generallibrary.ObjInfo self: """
        return not self.private() and str(self.name).startswith("_")




