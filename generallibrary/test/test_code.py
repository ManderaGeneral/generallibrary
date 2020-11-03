
import unittest

from generallibrary.versions import VerInfo
from generallibrary.code import clipboard_copy, clipboard_get


class CodeTest(unittest.TestCase):
    @unittest.skipIf(VerInfo().linux, "Clipboard - Couldn't get to work in linux VM, maybe works in normal linux environment.")
    def test_clipboard(self):
        clipboard_copy("foo")
        self.assertEqual("foo", clipboard_get())
        clipboard_copy("bar")
        self.assertEqual("bar", clipboard_get())
