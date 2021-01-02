
import unittest

from generallibrary.versions import VerInfo, package_is_installed
from generallibrary.code import clipboard_copy, clipboard_get, CodeLine, debug, print_link, print_link_to_obj, get_lines


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

        self.assertEqual(8, len(codeLine.get_lines()))
        codeLine.text()

    def test_debug(self):
        x, y, z = 1, 2, 3
        self.assertIn("y * z + 3 = 9", debug(locals(), "x + y", "y * z + 3", "x", "self"))

    def test_print_link(self):
        """ Hard to assert these methods truly work without manual check. """
        print_link("../code.py", 23)
        print_link("test_code.py", 23)
        print_link("test_code.py")
        print_link(line=23)
        print_link()

    def test_print_link_to_obj(self):
        self.assertIn("line 8", print_link_to_obj(CodeTest))
        self.assertIn("line 9", print_link_to_obj(CodeTest.test_clipboard))
        self.assertIn("unittest/__init__.py\", line 1", print_link_to_obj(unittest))

    def test_get_lines(self):
        import generallibrary
        get_lines(self.test_get_lines)
        get_lines(get_lines)
        get_lines(generallibrary)


