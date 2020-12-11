
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



test = ObjInfo()
objInfo = ObjInfo(test)




print(objInfo.get_parent(0))
# objInfo.generate_attributes()  # 1.1: HERE ** Store all attributes safely

