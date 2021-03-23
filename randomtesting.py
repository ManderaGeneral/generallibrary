
from generallibrary import *
from generalfile import Path

from pprint import pprint


def foo():
    """ bar
        hello """

print(ObjInfo(foo).doc(only_first_line=False))
print(ObjInfo(foo).doc(only_first_line=False))

