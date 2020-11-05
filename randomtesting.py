
from generallibrary import *

# print(getLocalFeaturesAsMD(locals(), "generallibrary"))





class _Foo:
    def __init__(self):
        self.random = 4
        self._req = 2

    @deco_default_self_args
    def _bar(self, random, *args, _req, extra=2):
        return random, _req


print(_Foo._bar)
print(_Foo()._bar)
_Foo()._bar(8, 9, 10, 11)  # HERE ** Dont understand why its getting 2x self





