
# import generallibrary
# import generalvector
# import generalfile
# import generalgui
# generallibrary.attributes_to_markdown(generallibrary)
# generallibrary.attributes_to_markdown(generalvector)
# generallibrary.attributes_to_markdown(generalfile)
# generallibrary.attributes_to_markdown(generalgui)


import sys
from generallibrary import ObjInfo
import inspect
import gc


class Test:
    x = []

    def __init__(self):
        self.hello = "there"

    def tests(self):
        for x in range(3):
            yield x

    class Foo:
        def bar(self):
            pass


def a():
    def b():
        pass
    return b



test = Test


print([objInfo for objInfo in ObjInfo(test).generate_attributes() if objInfo.is_instance()])
