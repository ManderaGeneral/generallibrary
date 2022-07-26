
from generallibrary import *

class A(Recycle, metaclass=AutoInitBases):
    _recycle_keys = {"foo": str}

    # def __init__(self, foo, bar):
    #     pass


class B(A):
    _recycle_keys = {"bar": str}

    def __init__(self, foo, bar):
        self.bar = bar

    def __repr__(self):
        return f"{self.foo} and {self.bar}"


aa = B("a", "a")
ab = B("a", "b")
ba = B("b", "a")

print(aa is ab)
print(aa is ba)

print(aa is B("a", "a"))
