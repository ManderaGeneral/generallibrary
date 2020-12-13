
from generallibrary import *


class _Foo:
    _attr = 5
    attr = 3

    def self(self):
        """ Not protected. """
        pass

    def _self(self):
        pass

    @classmethod
    def _cls(cls):
        pass

    @staticmethod
    def _static():
        pass

    @property
    def _property(self):
        return

objInfo = ObjInfo(_Foo().self)
print(objInfo.get_parent())  # 1: HERE **

