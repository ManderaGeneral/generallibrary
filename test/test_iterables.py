
import unittest

from generallibrary.iterables import iterable, depth, dictFirstValue, iterFirstValue, joinWithStr, addToListInDict

class IterablesTest(unittest.TestCase):
    def test_iterable(self):
        self.assertEqual(iterable(tuple()), [])
        self.assertEqual(iterable([]), [])
        self.assertEqual(iterable({}), [])
        self.assertEqual(iterable(tuple([5, 2])), [5, 2])
        self.assertEqual(iterable([5, 2]), [5, 2])
        self.assertEqual(iterable({"a": 5, "b": 2}), [5, 2])

        self.assertFalse(iterable(None))
        self.assertFalse(iterable(5))
        self.assertFalse(iterable("test"))
        self.assertFalse(iterable(51.2))
        self.assertFalse(iterable(True))

    def test_depth(self):
        self.assertEqual(depth(5), 0)

        self.assertEqual(depth([]), 0)
        self.assertEqual(depth([5]), 1)
        self.assertEqual(depth([5, 2]), 1)
        self.assertEqual(depth([[5, 3], 2]), 2)
        self.assertEqual(depth([{"a": 5}, 2]), 2)

        self.assertEqual(depth({}), 0)
        self.assertEqual(depth({"a": 5}), 1)
        self.assertEqual(depth({"a": [5, 3]}), 2)
        self.assertEqual(depth({"a": {"a": 5}}), 2)

    def test_dictFirstValue(self):
        self.assertRaises(TypeError, dictFirstValue, [])
        self.assertRaises(TypeError, dictFirstValue, 5)

        self.assertIsNone(dictFirstValue({}))
        self.assertEqual(dictFirstValue({"a": 5}), 5)
        self.assertEqual(dictFirstValue({"a": 5, "b": 5}), 5)

    def test_iterFirstValue(self):
        self.assertRaises(TypeError, iterFirstValue, "hello")
        self.assertRaises(TypeError, iterFirstValue, 5)

        self.assertIsNone(iterFirstValue({}))
        self.assertEqual(iterFirstValue({"a": 5}), 5)
        self.assertEqual(iterFirstValue({"a": 5, "b": 5}), 5)

        self.assertIsNone(iterFirstValue([]))
        self.assertEqual(iterFirstValue([5]), 5)
        self.assertEqual(iterFirstValue([5, 2, 3]), 5)

        self.assertIsNone(iterFirstValue(tuple()))
        self.assertEqual(iterFirstValue(tuple([5])), 5)
        self.assertEqual(iterFirstValue(tuple([5, 2, 3])), 5)

    def test_joinWithStr(self):
        self.assertRaises(TypeError, joinWithStr, ".", 5)
        self.assertRaises(TypeError, joinWithStr, ".", "asdf")

        self.assertEqual(joinWithStr(".", [1, 2, 3]), "1.2.3")
        self.assertEqual(joinWithStr(".", {"a": 1, "b": 2, "c": 3}), "1.2.3")
        self.assertEqual(joinWithStr(".", {"a": "1", "b": 2, "c": 3}), "1.2.3")
        self.assertEqual(joinWithStr(".", tuple([1, 2, 3])), "1.2.3")
        self.assertEqual(joinWithStr(".", [["foo", "bar"]]), "['foo', 'bar']")
        self.assertEqual(joinWithStr(".", [["foo", "bar"], ["foo", "bar"]]), "['foo', 'bar'].['foo', 'bar']")

    def test_addToListInDict(self):
        d = {}
        addToListInDict(d, "test", 5)
        self.assertEqual(d, {"test": [5]})

        addToListInDict(d, "test", 3)
        self.assertEqual(d, {"test": [5, 3]})

        addToListInDict(d, "test", None)
        self.assertEqual(d, {"test": [5, 3, None]})

        addToListInDict(d, "hello", "hi")
        self.assertEqual(d, {"test": [5, 3, None], "hello": ["hi"]})
















































