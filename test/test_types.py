
import unittest

from generallibrary.types import strToDynamicType, typeChecker

import pandas as pd

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
        self.assertRaises(TypeError, typeChecker, 5, "str")
        self.assertRaises(TypeError, typeChecker, 5.2, int)
        self.assertRaises(TypeError, typeChecker, 5.2, "int")
        self.assertRaises(TypeError, typeChecker, 5.2, [str, list])
        self.assertRaises(TypeError, typeChecker, 5.2, ["str", list])
        self.assertRaises(TypeError, typeChecker, 5.2, [str, "list"])
        self.assertRaises(TypeError, typeChecker, 5.2, ["str", "list"])
        self.assertRaises(TypeError, typeChecker, 5.2, [str, list], float)
        self.assertRaises(TypeError, typeChecker, 5.2, ["str", "list"], "float")

        self.assertFalse(typeChecker(["hello"], (tuple, dict), (bool, str), error=False))
        self.assertFalse(typeChecker(["hello"], ("tuple", dict), (bool, str), error=False))
        self.assertFalse(typeChecker(["hello"], (tuple, dict), str, error=False))
        self.assertFalse(typeChecker(["hello"], (tuple, "dict"), str, error=False))
        self.assertFalse(typeChecker(["hello"], (tuple, "dict"), "str", error=False))

        self.assertTrue(typeChecker(None, None))
        self.assertTrue(typeChecker(None, [None, str]))
        self.assertTrue(typeChecker(None, [None, "str"]))
        self.assertTrue(typeChecker(None, [list, None]))
        self.assertTrue(typeChecker(None, ["list", "None", None]))
        self.assertTrue(typeChecker(True, bool))
        self.assertTrue(typeChecker(True, "bool"))
        self.assertTrue(typeChecker(5, int))
        self.assertTrue(typeChecker(5, "int"))
        self.assertTrue(typeChecker(5, float))
        self.assertTrue(typeChecker(5, "floAt"))
        self.assertTrue(typeChecker(5, [None, float]))
        self.assertTrue(typeChecker(5, ["None", "float"]))
        self.assertTrue(typeChecker(5, ["None", float]))
        self.assertTrue(typeChecker(5, [None, "float"]))
        self.assertTrue(typeChecker(5, [str, float, None]))
        self.assertTrue(typeChecker(5, ["str", "float", "None"]))
        self.assertTrue(typeChecker(5, [str, float, "None"]))
        self.assertTrue(typeChecker(5, [str, "float", None]))
        self.assertTrue(typeChecker(5, ["str", float, None]))

        self.assertFalse(typeChecker(None, "None", error=False))
        self.assertFalse(typeChecker(None, bool, error=False))
        self.assertFalse(typeChecker(None, "bool", error=False))
        self.assertFalse(typeChecker(None, int, error=False))
        self.assertFalse(typeChecker(None, "int", error=False))
        self.assertFalse(typeChecker(True, None, error=False))
        self.assertFalse(typeChecker(True, "None", error=False))
        self.assertFalse(typeChecker(False, None, error=False))
        self.assertFalse(typeChecker(False, "None", error=False))

        self.assertTrue(typeChecker(tuple(["hello"]), (tuple, dict), str, error=False))
        self.assertTrue(typeChecker(tuple(["hello"]), ("Tuple", "dIct"), "sTr", error=False))
        self.assertTrue(typeChecker(tuple(["hello"]), (tuple, dict), "str", error=False))
        self.assertTrue(typeChecker(tuple(["hello"]), (tuple, "dict"), str, error=False))
        self.assertTrue(typeChecker(tuple(["hello"]), ("tuple", dict), str, error=False))

        self.assertTrue(typeChecker("hello", (bool, str)))
        self.assertTrue(typeChecker("hello", ("bool", "str")))
        self.assertTrue(typeChecker("hello", (bool, "str")))
        self.assertTrue(typeChecker("hello", ("bool", str)))

        self.assertTrue(typeChecker(["hello"], list, (bool, str)))
        self.assertTrue(typeChecker(["hello"], "list", ("bool", "str")))
        self.assertTrue(typeChecker(["hello"], list, (bool, "str")))
        self.assertTrue(typeChecker(["hello"], list, ("bool", str)))
        self.assertTrue(typeChecker(["hello"], "list", (bool, str)))

        self.assertTrue(typeChecker({"hello": [5, "hi"]}, dict, list, int))
        self.assertTrue(typeChecker({"hello": [5, "hi"]}, "dict", "list", "int"))
        self.assertTrue(typeChecker({"hello": [5, "hi"]}, dict, list, "int"))
        self.assertTrue(typeChecker({"hello": [5, "hi"]}, dict, "list", int))
        self.assertTrue(typeChecker({"hello": [5, "hi"]}, "dict", list, int))

        self.assertTrue(typeChecker(pd.DataFrame(), "dataframe"))
        self.assertFalse(typeChecker(pd.DataFrame(), "dataframes", error=False))
        self.assertTrue(typeChecker(pd.DataFrame(), pd.DataFrame))

        self.assertTrue(typeChecker(pd.DataFrame(), [None, pd.DataFrame]))
        self.assertTrue(typeChecker(pd.DataFrame(), [None, "dataframe"]))
        self.assertTrue(typeChecker(pd.DataFrame(), [int, None, pd.DataFrame]))


