
import unittest

from generallibrary.versions import VerInfo
from generallibrary.code import clipboard_copy, clipboard_get

unittest.skipIf(VerInfo.linux, "Couldn't get to work in linux VM, maybe works in normal linux environment.")
class CodeTest(unittest.TestCase):
    def test_clipboard(self):
        clipboard_copy("foo")
        self.assertEqual("foo", clipboard_get())
        clipboard_copy("bar")
        self.assertEqual("bar", clipboard_get())
