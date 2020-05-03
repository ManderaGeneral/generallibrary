
import unittest

from generallibrary.types import strToDynamicType, typeChecker

class TypesTest(unittest.TestCase):
    def test_strToDynamicType(self):
        self.assertIs(strToDynamicType("true"), True)
        self.assertIs(strToDynamicType("False"), False)
        self.assertIs(strToDynamicType("nOne"), None)

        self.assertEqual(strToDynamicType("5"), 5)
        self.assertEqual(strToDynamicType("5.2"), 5.2)
        self.assertEqual(strToDynamicType("0"), 0)
        self.assertEqual(strToDynamicType("-5.2"), -5.2)

        self.assertEqual(strToDynamicType("-5,2"), "-5,2")
        self.assertEqual(strToDynamicType("hello"), "hello")

    def test_typeChecker(self):
        self.assertRaises(TypeError, typeChecker, 5, str)
        self.assertRaises(TypeError, typeChecker, 5.2, int)
        self.assertRaises(TypeError, typeChecker, 5.2, [str, list])
        self.assertRaises(TypeError, typeChecker, 5.2, [str, list], float)

        self.assertFalse(typeChecker(["hello"], (tuple, dict), (bool, str), error=False))
        self.assertFalse(typeChecker(["hello"], (tuple, dict), str, error=False))

        self.assertTrue(typeChecker(5, int))
        self.assertTrue(typeChecker(5, float))
        self.assertTrue(typeChecker(tuple(["hello"]), (tuple, dict), str, error=False))
        self.assertTrue(typeChecker("hello", (bool, str)))
        self.assertTrue(typeChecker("hello", [bool, str]))
        self.assertTrue(typeChecker(["hello"], list, (bool, str)))

        self.assertTrue(typeChecker({"hello": [5, "hi"]}, dict, list, int))



