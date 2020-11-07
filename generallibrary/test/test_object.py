
import unittest

from generallibrary.object import getsize, initBases


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






































