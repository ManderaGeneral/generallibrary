
import unittest

from generallibrary.types import typeChecker

class TypesTest(unittest.TestCase):
    def test_strToDynamicType(self):
        pass

    def test_typeChecker(self):
        self.assertTrue(typeChecker("hello", (bool, str)))
        self.assertTrue(typeChecker(["hello"], list, (bool, str)))
        self.assertFalse(typeChecker(["hello"], (tuple, dict), (bool, str), raiseTypeError=False))
