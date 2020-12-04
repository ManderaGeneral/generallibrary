
# import generallibrary
# import generalvector
# import generalfile
# import generalgui
# generallibrary.attributes_to_markdown(generallibrary)
# generallibrary.attributes_to_markdown(generalvector)
# generallibrary.attributes_to_markdown(generalfile)
# generallibrary.attributes_to_markdown(generalgui)

from generallibrary import ObjInfo

import inspect
import sys

class Test:
    def tests(self):
        pass

    class Foo:
        def bar(self):
            pass

def a():
    def b():
        pass
    return b


# print(ObjInfo(Test.tests).get_parent().obj)
# print(ObjInfo(Test().tests).get_parent().obj)

print(ObjInfo(a).is_method())
