
from generallibrary import *



class A(Recycle):
    # _recycle_keys = {}
    _recycle_keys = {"foo": str}

    def __init__(self, foo):
        pass

print(A(1) is A(foo=1))
print(A(2) is A(foo=1))

# def x(y):
#     print(y)
#
# def x2(foo):
#     print(foo)
#
# SigInfo(x, 5).call(x2)


# class C(Recycle):
#     _recycle_keys = {"x": str}
#     def __init__(self, x):
#         pass
#
# print(C(1) is C(2))


