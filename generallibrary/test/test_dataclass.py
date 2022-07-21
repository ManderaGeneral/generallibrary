
from generallibrary.objinfo.objinfo import DataClass
from unittest import TestCase

class DataClassTest(TestCase):
    def test_field_keys(self):
        class A(DataClass):
            x = 5
        self.assertEqual(["x"], A.field_keys())

        class B(A):
            y = "foo"
        self.assertCountEqual(["x", "y"], B.field_keys())

        class A(DataClass):
            foo: str = "hi"
            bar = ["there"]
            _private = "six"

        self.assertCountEqual(["foo", "bar"], A.field_keys())

    def test_field_default_values(self):
        class A(DataClass):
            x = 5
        self.assertEqual([5], A.field_values_defaults())

        class B(A):
            y = "foo"
        self.assertCountEqual(["foo", 5], B.field_values_defaults())

        class A(DataClass):
            foo: str = "hi"
            bar = [True]
            _private = "six"

        self.assertCountEqual(["hi", [True]], A.field_values_defaults())

    def test_field_default_dict(self):
        class A(DataClass):
            x = 5
        self.assertEqual({"x": 5}, A.field_dict_defaults())

        class B(A):
            y = "foo"
        self.assertEqual({"y": "foo", "x": 5}, B.field_dict_defaults())

        class A(DataClass):
            foo: str = "hi"
            bar = [True]
            _private = "six"

        self.assertEqual({"foo": "hi", "bar": [True]}, A.field_dict_defaults())

    def test_field_annotations_dict(self):
        class A(DataClass):
            x = 5
        self.assertEqual({}, A.field_dict_annotations())

        class B(A):
            y = "foo"
        self.assertEqual({}, B.field_dict_annotations())

        class A(DataClass):
            foo: str = "hi"
            bar = [True]
            _private = "six"

        self.assertEqual({"foo": str}, A.field_dict_annotations())

    def test_field_values(self):
        class A(DataClass):
            x = 5
        a = A()
        self.assertEqual([5], a.field_values())
        a.x = 3
        self.assertEqual([3], a.field_values())

        class B(A):
            y = "foo"
        a = B()

        self.assertCountEqual([5, "foo"], a.field_values())
        a.x = 3
        self.assertCountEqual([3, "foo"], a.field_values())
        a.y = True
        self.assertCountEqual([3, True], a.field_values())

        class A(DataClass):
            foo: str = "hi"
            bar = [True]
            _private = "six"
        a = A()

        self.assertCountEqual(["hi", [True]], a.field_values())
        a._private = "yo"
        self.assertCountEqual(["hi", [True]], a.field_values())

    def test_field_dict(self):
        class A(DataClass):
            x = 5
        a = A()
        self.assertEqual({"x": 5}, a.field_dict())
        a.x = 3
        self.assertEqual({"x": 3}, a.field_dict())

        class B(A):
            y = "foo"
        a = B()

        self.assertCountEqual({"x": 5, "y": "foo"}, a.field_dict())
        a.x = 3
        self.assertCountEqual({"x": 3, "y": "foo"}, a.field_dict())
        a.y = True
        self.assertCountEqual({"x": 3, "y": True}, a.field_dict())

        class A(DataClass):
            foo: str = "hi"
            bar = [True]
            _private = "six"
        a = A()

        self.assertCountEqual({"foo": "hi", "bar": [True]}, a.field_dict())
        a._private = "yo"
        self.assertCountEqual({"foo": "hi", "bar": [True]}, a.field_dict())
        a.new_one = "hii"
        self.assertCountEqual({"foo": "hi", "bar": [True]}, a.field_dict())












