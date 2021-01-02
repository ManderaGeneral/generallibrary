
import unittest

from generallibrary.object import getsize, initBases
from generallibrary import ObjInfo
from generallibrary.objinfo.type import _ObjInfoType


class ObjectTest(unittest.TestCase):
    def test_getsize(self):
        """Hard to make too specific tests I think due to 64-bit vs 32-bit for example."""
        x = []
        y = "hi"
        z = [y]
        self.assertGreater(getsize(z), getsize(x) + getsize(y))  # See that there's overhead

    def test_initBases(self):
        # One argument without default
        class Base:
            def __init__(self, x):
                self.x = x

        @initBases
        class Parent(Base):
            def __init__(self, x):
                self.y = 2

        self.assertEqual(5, Parent(x=5).x)
        self.assertEqual(5, Parent(5).x)
        self.assertEqual(2, Parent(x=5).y)
        self.assertEqual(2, Parent(5).y)

        # One argument without default and one value with default inside Base
        class Base:
            def __init__(self, x, z=6):
                self.x = x
                self.z = z

        @initBases
        class Parent(Base):
            def __init__(self, x, z=None):
                self.y = 2
        self.assertEqual(5, Parent(x=5).x)
        self.assertEqual(2, Parent(x=5).y)
        self.assertIs(None, Parent(x=5).z)
        self.assertEqual(4, Parent(x=5, z=4).z)

        # One argument without default and one value with default inside Parent
        class Base:
            def __init__(self, x, z):
                self.x = x
                self.z = z

        @initBases
        class Parent(Base):
            def __init__(self, x, z=None):
                self.y = 2

        self.assertEqual(5, Parent(x=5).x)
        self.assertEqual(2, Parent(x=5).y)
        self.assertEqual(None, Parent(x=5).z)
        self.assertEqual(4, Parent(x=5, z=4).z)

        # Base without init
        class Base:
            def test(self):
                pass

        @initBases
        class Parent(Base):
            def __init__(self, x):
                self.x = x
                self.y = 2

        self.assertEqual(5, Parent(x=5).x)
        self.assertEqual(2, Parent(x=5).y)

        # Two bases, seperate args
        class Base:
            def __init__(self, x):
                self.x = x

        class Base2:
            def __init__(self, y):
                self.y = y

        @initBases
        class Parent(Base, Base2):
            def __init__(self, x, y):
                pass

        self.assertEqual(5, Parent(x=5, y=2).x)
        self.assertEqual(2, Parent(x=5, y=2).y)

        # Two bases, same args
        class Base:
            def __init__(self, x):
                self.x = x
        class Base2:
            def __init__(self, x):
                self.y = x

        @initBases
        class Parent(Base, Base2):
            def __init__(self, x):
                pass

        self.assertEqual(5, Parent(x=5).x)
        self.assertEqual(5, Parent(x=5).y)

        # One base taking *args
        class Base:
            def __init__(self, *x):
                self.x = x

        @initBases
        class Parent(Base):
            def __init__(self, *x):
                pass
        self.assertEqual((5, ), Parent(5).x)

    def test_hierarchy(self):
        class C:
            def __init__(self, c, d=4):
                self.c = c
                self.d = d

        @initBases
        class B(C):
            def __init__(self, b, c):
                self.b = b

        @initBases
        class A(B):
            def __init__(self, b, c):
                pass

        a = A(b=2, c=3)

        self.assertEqual(2, a.b)
        self.assertEqual(3, a.c)
        self.assertEqual(4, a.d)

        self.assertEqual(1, A(1, 2).b)
        self.assertEqual(1, A(1, c=2).b)

    def test_hierarchy_empty_middleman(self):
        class C:
            def __init__(self, a, b=2):
                self.a = a
                self.b = b

        @initBases
        class B(C):
            pass

        @initBases
        class A(B):
            def __init__(self, a, b=None):
                pass

        self.assertEqual(5, A(5).a)
        self.assertEqual(5, A(a=5).a)

        self.assertEqual(None, A(5).b)

    def test__init_post__(self):
        glob = []

        class A:
            def __init__(self):
                glob.append(1)

            def __init_post__(self):
                glob.append(4)

        @initBases
        class B(A):
            def __init__(self):
                glob.append(2)

            def __init_post__(self):
                glob.append(5)

        @initBases
        class C(B):
            def __init__(self):
                glob.append(3)

            def __init_post__(self):
                glob.append(6)

        C()
        self.assertEqual([1, 2, 3, 4, 5, 6], glob)

    def test_ObjInfo(self):
        def check(bound_method):
            """ Check that the correct method is True and all other are False. """
            objInfo = getattr(bound_method, "__self__")
            for name, method in objInfo.type_methods.items():
                method_is_bound_method = bound_method == getattr(objInfo, name)
                result = method(self=objInfo)
                if result is not method_is_bound_method:
                    raise AssertionError(f"{objInfo} returns {result} for {name}.")


        check(ObjInfo(unittest).is_module)
        check(ObjInfo(a).is_function)
        check(ObjInfo(a()).is_function)
        check(ObjInfo(_Foo).is_class)
        check(ObjInfo(_Foo()).is_instance)

        check(ObjInfo(_Foo._self).is_method)
        check(ObjInfo(_Foo()._self).is_method)

        check(ObjInfo(_Foo._cls).is_method)
        check(ObjInfo(_Foo()._cls).is_method)

        check(ObjInfo(_Foo._static).is_method)
        check(ObjInfo(_Foo()._static).is_method)

        check(ObjInfo(_Foo._property).is_property)

    def test_ObjInfo_parents(self):
        objInfo = ObjInfo(ObjInfo)
        self.assertEqual("generallibrary", objInfo.get_parent(-1).obj.__name__)

    def test_ObjInfo_protected(self):
        objInfo = ObjInfo(_Foo)
        objInfo.filters = []
        objInfo.get_attrs()

        self.assertEqual(True, objInfo.get_child_by_key_values(name="_self").protected())
        self.assertEqual(False, objInfo.get_child_by_key_values(name="self").protected())

        self.assertEqual(True, objInfo.get_child_by_key_values(name="_attr").protected())
        self.assertEqual(False, objInfo.get_child_by_key_values(name="attr").protected())

        self.assertEqual(False, objInfo.get_child_by_key_values(name="_Foo__private").protected())
        self.assertEqual(True, objInfo.get_child_by_key_values(name="_Foo__private").private())
        self.assertEqual(True, objInfo.get_child_by_key_values(name="_Foo__private").internal())
        self.assertEqual(False, objInfo.get_child_by_key_values(name="_Foo__private").public())

        self.assertEqual(False, ObjInfo(a).protected())
        self.assertEqual(False, ObjInfo(a()).protected())


class _Foo:
    _attr = 5
    attr = 3

    def self(self):
        """ Not protected. """
        pass

    def _self(self):
        pass

    @classmethod
    def _cls(cls):
        pass

    @staticmethod
    def _static():
        pass

    @property
    def _property(self):
        return

    def __private(self):
        pass


def a():
    def b():
        pass
    return b

















