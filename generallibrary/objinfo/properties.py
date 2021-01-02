
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

    def module(self):
        """ Return module of this ObjInfo's obj as returned by inspect or None.

            :param generallibrary.ObjInfo self: """
        return inspect.getmodule(self.obj)

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





