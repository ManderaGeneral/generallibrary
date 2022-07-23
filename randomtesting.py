
from generallibrary import *

class A(Recycle):
    _recycle_keys = {"foo": str}

class B(A):
    pass


print(A())
print(B())
