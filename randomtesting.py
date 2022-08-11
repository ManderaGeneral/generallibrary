
from generallibrary import *


# Allow recycle_keys to use any key, not only key correlating with parameter name
# Allow more than two parameters for recycle_key functions

def x(foo, bar, cls):
    print(foo, bar, cls)
    return 5

class A(Recycle):
    # _recycle_keys = {}
    _recycle_keys = {"foo": x}

    def __init__(self, foo, bar):
        pass


# print(A(1) is A(foo=1))
# print(A(2) is A(foo=1))

# def x(y):
#     print(y)
#
# def x2(foo):
#     print(foo)
#
# # SigInfo(x, 5).call(x2)
#
# class X:
#     def __init__(self, y):
#         print(y)
#
# sig = SigInfo(X.__init__, 5)
#
# print(sig.names)
# sig.call(x2)
#
# print(X)



# class C(Recycle):
#     _recycle_keys = {"x": str}
#     def __init__(self, x):
#         pass
#
# print(C(1) is C(2))


