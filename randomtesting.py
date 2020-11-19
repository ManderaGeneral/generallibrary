
# from generallibrary import *

# print(getLocalFeaturesAsMD(locals(), "generallibrary"))




# class Attr:
#     def __init__(self, ):
#         pass


def attributes(cls_or_instance, properties=True, methods=True, variables=True, protected=False, from_instance=True, from_class=True, from_bases=False):
    if isinstance(cls_or_instance, type):
        cls = cls_or_instance
        instance = None
    else:
        cls = cls_or_instance.__class__
        instance = cls_or_instance

    attrs = {}
    for key in dir(cls_or_instance):
        cls_attr = getattr(cls, key, None)
        is_property = isinstance(cls_attr, property)
        is_protected = key.startswith("_")
        attr = cls_attr if is_property else getattr(cls_or_instance, key)

        # Property, Method and Variable
        if properties is False and is_property:
            continue
        elif methods is False and callable(attr):
            continue
        elif variables is False:
            continue

        # Protected
        if protected is False and is_protected:
            continue
        elif protected is True and not is_protected:
            continue




        attrs[key] = attr
    return attrs

class Foo:
    @property
    def a(self):
        print(5)
        return

print(attributes(Foo()))
