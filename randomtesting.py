
# import generallibrary
# import generalvector
# import generalfile
# import generalgui
# generallibrary.attributes_to_markdown(generallibrary)
# generallibrary.attributes_to_markdown(generalvector)
# generallibrary.attributes_to_markdown(generalfile)
# generallibrary.attributes_to_markdown(generalgui)


from generallibrary import attributes, TreeDiagram

class DefTreeNode(TreeDiagram):
    """ A TreeDiagram containing an object's recursive definitions.
        Intended for modules, functions, classes and attributes. """
    def __init__(self, obj):
        self.obj = obj

    @property  # HERE ** fix this lovely class
    def doc_lines(self):
        return str(obj.__doc__).split("\n")

    @property
    def explanation(self):
        doc_lines[1 if not doc_lines[0] and len(doc_lines) > 1 else 0]
        return re.sub(r"^ +| +$", "", explanation)

    @property
    def attr_is_cls(self):
        return isinstance(attr, type)

    @property
    def type_name(self):
        return "property" if is_property else "class" if attr_is_cls else attr.__class__.__name__

    @property
    def name(self):
        return key

    @property
    def module(self):
        return getattr(obj, "__module__", "")


    def _get_attributes(self, obj):
        """ Helper for attributes_to_markdown. """
        return attributes(obj, from_bases=True)

    def get_definitions_diagram(self, obj, allow_bad_docs=False, printed_objs=None, print_out=True, return_lines=True):

        obj_is_class = isinstance(obj, type)

        if printed_objs is None:
            printed_objs = [obj]
        else:
            printed_objs.append(obj)

        for key, attr in _get_attributes(obj).items():
            if is_property := isinstance(attr, property):
                attr = attr.fget
            module = getattr(attr, "__module__", "")
            doc_lines = str(attr.__doc__).split("\n")
            explanation = doc_lines[1 if not doc_lines[0] and len(doc_lines) > 1 else 0]
            explanation = re.sub(r"^ +| +$", "", explanation)
            attr_is_cls = isinstance(attr, type)
            type_name = "property" if is_property else "class" if attr_is_cls else attr.__class__.__name__
            name = key
            attrs_count = 0

            # If attr is a variable
            if not module:
                type_name, explanation = "variable", f"Variable of type '{type_name}'."

            # If attr is a method
            if obj_is_class and type_name == "function":
                type_name = "method"

            if attr_is_cls:
                cls = attr
                attrs = _get_attributes(cls)
                if attrs and cls not in classes and cls is not obj:
                    classes.append(cls)
                    name = f"[{key}]({_get_header_from_obj(cls, link=True)})"
                    attrs_count = len(attrs)

            rows.append({
                "Module": module.split(".")[-1],
                "Name":  name,
                "Type": type_name,
                "Attributes": attrs_count,
                "Explanation": explanation,
            })

