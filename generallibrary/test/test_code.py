
from generallibrary.code import *
from generallibrary.versions import VerInfo

import unittest


class CodeTest(unittest.TestCase):
    @unittest.skipIf(VerInfo().linux, "Clipboard - Couldn't get to work in linux VM, maybe works in normal linux environment.")
    def test_clipboard(self):
        clipboard_copy("foo")
        self.assertEqual("foo", clipboard_get())
        clipboard_copy("bar")
        self.assertEqual("bar", clipboard_get())

    def test_CodeLine(self):
        codeLine = CodeLine()
        CodeLine("print(5)", parent=codeLine)
        codeLine2 = CodeLine("print(5)", space_before=1, parent=codeLine)
        CodeLine("print(5)", space_after=2, parent=codeLine2)

        self.assertEqual(9, len(codeLine.get_lines()))

    def test_debug(self):
        x, y, z = 1, 2, 3
        self.assertIn("y * z + 3 = 9", debug(locals(), "x + y", "y * z + 3", "x", "self", print_out=False))

    def test_print_link(self):
        """ Hard to assert these methods truly work without manual check. """
        print_link("../code.py", 23, print_out=False)
        print_link("test_code.py", 23, print_out=False)
        print_link("test_code.py", print_out=False)
        print_link(line=23, print_out=False)
        print_link(print_out=False)

    def test_print_link_to_obj(self):
        self.assertIn("line 8", print_link_to_obj(CodeTest, print_out=False))
        self.assertIn("line 16", print_link_to_obj(CodeTest.test_CodeLine, print_out=False))
        self.assertIn("unittest/__init__.py\", line 1", print_link_to_obj(unittest, print_out=False))

    def test_warn(self):
        self.assertIn("line 42", warn("foo", print_out=False))

