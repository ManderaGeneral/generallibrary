
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

class Test(ObjInfo):
    def tests(self):
        pass

    class Foo:
        def bar(self):
            pass


print(Test.get_parent.__module__)
print(Test.tests.__module__)

print(Test.get_parent.__qualname__)
print(Test.tests.__qualname__)

# print(sys.modules.get("generallibrary.object"))

# objInfo = ObjInfo(Test)



