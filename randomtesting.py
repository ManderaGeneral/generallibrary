
from generallibrary import *

# print(getLocalFeaturesAsMD(locals(), "generallibrary"))



# class C:
#     def __init__(self, b):
#         self.b = b
#
# @initBases  # Wrap init with new signature (*args, **kwargs). Call C with all args it can take. (a)
# class B(C):
#     pass
#
# @initBases
# class A(B):  # Wrap init with new signature (*args, **kwargs). Call B with all args it can take. (*args, **kwargs)
#     def __init__(self, a, b):
#         self.a = a


class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b

@initBases
class A(B):
    def __init__(self, a, b=None):
        pass

a = A(a=2)
print(a.a, a.b)




# func is unbound!
# def deco(func):
#     def _wrapper(*args, **kwargs):
#         print(func, args, kwargs)
#         return func(*args, **kwargs)
#     return _wrapper
#
#
# class Test:
#     @deco
#     def a(self):
#         pass



# def deco(cls):
#     func = cls.a
#
#     def _wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#
#     cls.a = _wrapper
#     return cls
#
# import inspect



# @deco
# class Test:
#     def a(self):
#         pass
#
# bound = Test().a
# unbound = Test.a
#
# print(bound)
# print(unbound)

# for func in (bound, unbound):
#     print(list(inspect.signature(func).parameters.values()))

"""
A bound method does not have a ´self´ parameter.
Use slash to allow ´self´ in kwargs
"""



# class Test:
#     def a(self, /, b, **kwargs):
#         print(self, b, kwargs)
#
#
# print(list(inspect.signature(Test.a).parameters.values()))
# Test().a("foo", self="bar")
















