
import unittest

from generallibrary.types import strToDynamicType, typeChecker, getBaseClasses, getBaseClassNames, hasMethod, HierarchyStorer


class InheritStr(str):
    pass

class TypesTest(unittest.TestCase):
    def test_strToDynamicType(self):
        self.assertIs(strToDynamicType("True"), True)
        self.assertIs(strToDynamicType("False"), False)
        self.assertIs(strToDynamicType("None"), None)

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

        self.assertTrue(typeChecker(InheritStr(), "InheritStr"))
        self.assertFalse(typeChecker(InheritStr(), "InheritStrs", error=False))
        self.assertTrue(typeChecker(InheritStr(), InheritStr))

        self.assertTrue(typeChecker(InheritStr(), [None, InheritStr]))
        self.assertTrue(typeChecker(InheritStr(), [None, "InheritStr"]))
        self.assertTrue(typeChecker(InheritStr(), [int, None, InheritStr]))

        self.assertTrue(typeChecker(InheritStr(), str))
        self.assertTrue(typeChecker(InheritStr(), "str"))

        self.assertTrue(typeChecker(True, "bool"))
        self.assertTrue(typeChecker(True, "object"))
        self.assertTrue(typeChecker(True, object))

        self.assertFalse(typeChecker(True, int, error=False))
        self.assertFalse(typeChecker(True, "int", error=False))

    def test_getBasesClasses(self):
        self.assertEqual([int, object], getBaseClasses(True))
        self.assertEqual(["int", "object"], getBaseClassNames(True))

        self.assertEqual([object], getBaseClasses(5))
        self.assertEqual(["object"], getBaseClassNames(5))

        self.assertEqual([bool, int, object], getBaseClasses(True, includeSelf=True))
        self.assertEqual(["bool", "int", "object"], getBaseClassNames(True, includeSelf=True))

        self.assertEqual([int, object], getBaseClasses(5, includeSelf=True))
        self.assertEqual(["int", "object"], getBaseClassNames(5, includeSelf=True))

    def test_hasMethod(self):
        self.assertEqual(True, hasMethod([], "append"))
        self.assertEqual(False, hasMethod([], "appends"))

        self.assertEqual(True, hasMethod("hello", "lower"))
        self.assertEqual(False, hasMethod("hello", "lowers"))

        self.assertEqual(True, hasMethod("hello", "__contains__"))
        self.assertEqual(False, hasMethod("hello", "__module__"))

    def test_HierarchyStorer(self):
        class Base(metaclass=HierarchyStorer, base="Base"):
            pass
        class A(Base):
            pass
        class B(A):
            pass

        self.assertIs(A, Base.A)
        self.assertIs(B, Base.B)
        self.assertIs(Base, A.Base)
        self.assertIs(Base, B.Base)





























