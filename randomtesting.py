
# import generallibrary
# import generalvector
# import generalfile
# import generalgui
# generallibrary.attributes_to_markdown(generallibrary)
# generallibrary.attributes_to_markdown(generalvector)
# generallibrary.attributes_to_markdown(generalfile)
# generallibrary.attributes_to_markdown(generalgui)

from generallibrary import ObjInfo


class Test:
    x = []
    def tests(self):
        pass

    class Foo:
        def bar(self):
            pass


def a():
    def b():
        pass
    return b



# objInfo = ObjInfo(Test())
# objInfo.generate_attributes()  # 1.1: HERE ** Store all attributes safely


# print(objInfo.get_parent())
# print(objInfo.get_children())
