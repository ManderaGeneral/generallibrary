
from generallibrary import deco_propagate_while

import inspect


class _ObjInfoProperties:
    def public(self):
        """ Get whether possible name is for public use, False if name is None.
            Opposite of internal.

            :param generallibrary.ObjInfo self: """
        return not self.internal()

    def internal(self):
        """ Get whether possible name is for internal use, False if name is None.
            True if private or protected.
            Opposite of public.

            :param generallibrary.ObjInfo self: """
        return self.private() or self.protected()

    def private(self):
        """ Get whether possible name is private, False if name is None.
            Subset of ObjInfo.internal().

            :param generallibrary.ObjInfo self: """
        return "__" in str(self.name)

    def protected(self):
        """ Get whether possible name is protected, False if name is None.
            Subset of ObjInfo.internal().

            :param generallibrary.ObjInfo self: """
        return not self.private() and str(self.name).startswith("_")

    @deco_propagate_while(value=None, prop=lambda objInfo: objInfo.get_parent())
    def module(self):
        """ Return module of this ObjInfo's obj as returned by inspect or None.

            :param generallibrary.ObjInfo self: """
        return inspect.getmodule(self.obj)

    def file(self, relative=False):
        """ Return str file of this ObjInfo's obj as returned by inspect or None.

            :param generallibrary.ObjInfo self:
            :param relative: Whether to return a relative path by splitting on top module's name. """
        obj, _ = self.get_original_obj_and_depth()
        file = inspect.getfile(obj)
        if relative:
            top_module = self.get_parent(-1)
            if top_module is None:
                top_module = self
            split_file = file.split(top_module.name)
            file = f"{top_module.name}{split_file[-1]}"
        return file

    def get_original_obj_and_depth(self, print_out=True):
        """ Relaying to function.

            :param generallibrary.ObjInfo self: """
        from generallibrary.code import get_original_obj_and_depth

        return get_original_obj_and_depth(self.obj)

    def print_link_to_obj(self, print_out=True):
        """ Relaying to function.

            :param generallibrary.ObjInfo self:
            :param print_out: """
        from generallibrary.code import print_link_to_obj

        return print_link_to_obj(self.obj, print_out=print_out)

    def get_definition_line(self):
        """ Relaying to function.

            :param generallibrary.ObjInfo self: """
        from generallibrary.code import get_definition_line

        return get_definition_line(self.obj)

    def get_lines(self):
        """ Relaying to function.

            :param generallibrary.ObjInfo self: """
        from generallibrary.code import get_lines

        return get_lines(self.obj)

    def doc(self, only_first_line=False, require_sentence=False):
        """ Return documentation string of this ObjInfo's obj.

            :param generallibrary.ObjInfo self:
            :param only_first_line: Whether to only return first line.
            :param require_sentence: Whether to require properly formatted lines. """
        from generallibrary.code import print_link_to_obj

        doc = inspect.getdoc(self.obj)

        if doc is None:
            doc = ""

        if doc and only_first_line:
            doc = doc.splitlines()[0]

        doc = doc.removesuffix(" ")

        if require_sentence:
            if not doc or not doc.endswith(".") or not doc[0].isupper():
                raise AttributeError(f"'{doc}' is not a proper a sentence from '{print_link_to_obj(self.obj, print_out=False)}'.")

        return doc





