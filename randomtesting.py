from generallibrary import *

from generalpackager import Packager

from functools import partial


def x(a, b):
    print(a, b)

y = partial(x, 2)
y()


class deco:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        print(instance, owner)
        return lambda *args, **kwargs: self.__call__(instance, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


# def deco(func):
#     def _wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return _wrapper


class X:
    @deco
    def y(self):
        print("hi")

X().y()



# Packager("generallibrary").localrepo.metadata.write_config()
#
# print(Packager("generallibrary").localrepo.metadata.extras_require)