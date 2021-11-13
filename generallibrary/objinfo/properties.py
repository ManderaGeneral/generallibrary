

from generallibrary.functions import deco_propagate_while
from generallibrary.types import getBaseClasses

import inspect
import re


class _ObjInfoProperties:
    def public(self):
        """ 0 leading underscores.
            Get whether possible name is for public use, False if name is None.
            Opposite of internal.

            :param generallibrary.ObjInfo self: """
        return not self.internal()

    def internal(self):
        """ 1 or 2 leading underscores.
            Get whether possible name is for internal use, False if name is None.
            True if private or protected.
            Opposite of public.

            :param generallibrary.ObjInfo self: """
        return self.private() or self.protected()

    def private(self):
        """ 2 leading underscores.
            Get whether possible name is private, False if name is None.
            Subset of ObjInfo.internal().

            :param generallibrary.ObjInfo self: """
        return "__" in str(self.name)

    def protected(self):
        """ 1 leading underscore.
            Get whether possible name is protected, False if name is None.
            Subset of ObjInfo.internal().

            :param generallibrary.ObjInfo self: """
        return not self.private() and str(self.name).startswith("_")

    @deco_propagate_while(value=None, prop_func=lambda objInfo: objInfo.get_parent())
    def module(self):
        """ Return module of this ObjInfo's obj as returned by inspect or None.

            :param generallibrary.ObjInfo self: """
        return self._module()

    def _module(self):
        return inspect.getmodule(self.obj)

    def file(self, relative=False):
        """ Return str file of this ObjInfo's obj as returned by inspect or None.

            :param generallibrary.ObjInfo self:
            :param relative: Whether to return a relative path by splitting on top module's name. """
        obj = self.origin
        try:
            file = inspect.getfile(obj)
        except TypeError:
            return

        if relative:
            top_module = self.get_parent(depth=-1, index=-1)
            if top_module is None:
                top_module = self
            split_file = file.split(top_module.name)
            file = f"{top_module.name}{split_file[-1]}"
        return file

    def print_link_to_obj(self, print_out=True):
        """ Relaying to function.

            :param generallibrary.ObjInfo self:
            :param print_out: """
        from generallibrary.code import print_link_to_obj

        return print_link_to_obj(self.obj, print_out=print_out)

    @classmethod
    def get_origin(cls, obj, include_depth=False):
        """ Relaying to function. """
        from generallibrary.code import get_origin

        return get_origin(obj=obj, include_depth=include_depth)

    def get_definition_line(self):
        """ Relaying to function with added error hiding.

            :param generallibrary.ObjInfo self: """
        from generallibrary.code import get_definition_line

        # return get_definition_line(self.obj)
        try:
            return get_definition_line(self.obj)
        except (TypeError, OSError):
            return 1

    def get_lines(self):
        """ Return a list of source lines from an obj.
            Used to extract todos.
            Experimental. Works on modules, classes and functions available to `inspect`.

            :param generallibrary.ObjInfo self: """
        lines = []
        for objInfo in self.get_all():
            if objInfo.is_class() or objInfo.is_function():
                obj_lines = inspect.getsourcelines(objInfo.obj)[0]
                lines.extend([line for line in obj_lines if not re.match("^( *)?\\n$", line)])
        return lines

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

        if doc.endswith(" "):
            doc = doc[:-1]

        if require_sentence:
            if not doc or not doc.endswith(".") or not doc[0].isupper():
                raise AttributeError(f"'{doc}' is not a proper a sentence from '{print_link_to_obj(self.obj, print_out=False)}'.")

        return doc

    def defined_by_parent(self):
        """ Get whether obj is defined directly by it's parent by seeing if it's unique from parent's base classes'.

            :param generallibrary.ObjInfo self: """
        if self.get_parent() is None:
            return False

        for base in getBaseClasses(self.get_parent().obj):
            base_obj = getattr(base, self.name, None)
            if self.obj is base_obj:
                return False
        return True



