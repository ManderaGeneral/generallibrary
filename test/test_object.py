
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
        self.assertRaises(AttributeError, Parent)
        self.assertRaises(AttributeError, Parent, doesntExist=5)
        self.assertRaises(TypeError, Parent, 5)

        self.assertEqual(5, Parent(x=5).x)
        self.assertEqual(2, Parent(x=5).y)

        # One argument without default and one value with default inside Base
        class Base:
            def __init__(self, x, z=6):
                self.x = x
                self.z = z
        @initBases
        class Parent(Base):
            def __init__(self, x, z=None):
                self.y = 2
        self.assertRaises(AttributeError, Parent)
        self.assertRaises(AttributeError, Parent, y=5)
        self.assertRaises(AttributeError, Parent, x=5, y=3, doesntExist=2)
        self.assertRaises(TypeError, Parent, 3, y=5)

        self.assertEqual(5, Parent(x=5).x)
        self.assertEqual(2, Parent(x=5).y)
        self.assertEqual(6, Parent(x=5).z)
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
        self.assertRaises(AttributeError, Parent)
        self.assertRaises(AttributeError, Parent, y=5)
        self.assertRaises(AttributeError, Parent, x=5, y=3, doesntExist=2)
        self.assertRaises(TypeError, Parent, 3, y=5)

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
        self.assertRaises(AttributeError, Parent)
        self.assertRaises(AttributeError, Parent, y=5)
        self.assertRaises(AttributeError, Parent, x=5, y=3, doesntExist=2)
        self.assertRaises(TypeError, Parent, 3, y=5)

        self.assertEqual(5, Parent(x=5).x)
        self.assertEqual(2, Parent(x=5).y)














































