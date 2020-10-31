
import unittest

from generallibrary.code import clipboard_copy, clipboard_get


class CodeTest(unittest.TestCase):
    def test_clipboard(self):
        clipboard_copy("foo")
        self.assertEqual("foo", clipboard_get())
        clipboard_copy("bar")
        self.assertEqual("bar", clipboard_get())
