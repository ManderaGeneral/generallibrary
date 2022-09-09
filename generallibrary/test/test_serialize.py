
import generallibrary
from generallibrary.serialize import *

import unittest


class SerializeTest(unittest.TestCase):
    def test_serialize(self):
        x = ["hi"]
        self.assertEqual(x, loads(dumps(x)))

        x = ["hi", ["there"]]
        self.assertEqual(x, loads(dumps(x)))

    def test_serialize_custom_obj(self):
        class X:
            def __init__(self, y):
                self.y = y
        x = X(5)
        self.assertEqual(5, loads(dumps(x), locals()).y)

        x = {"a": X(5)}
        self.assertEqual(5, loads(dumps(x), locals())["a"].y)

    def test_serialize_custom_obj_no_init(self):
        class X:
            pass
        x = X()
        x.a = 3
        self.assertEqual(3, loads(dumps(x), locals()).a)

    def test_serialize_cls(self):
        class X:
            pass
        self.assertEqual(X, loads(dumps(X), locals()))

        class X:
            y = 2
        self.assertEqual(2, loads(dumps(X), locals()).y)

        X.y = "hi"
        self.assertEqual("hi", loads(dumps(X), locals()).y)

    def test_serialize_cls_and_instance_attrs(self):
        class X:
            y = 2
            def __init__(self, z):
                self.z = z
        a = X(4)
        b = loads(dumps(X(4)), locals())
        self.assertEqual((4, 2), (b.z, b.y))

    def test_serialize_mix(self):
        class X:
            def __init__(self, y):
                self.y = y
            def __eq__(self, other):
                return self.y == other.y

        x = ["hi", 5, None, {"ab": X(3), "2": "hi"}]
        self.assertEqual(x, loads(dumps(x), locals()))
