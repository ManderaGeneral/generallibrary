
import unittest

from generallibrary.iterables import getIterable, isIterable, depth, dictFirstValue, iterFirstValue, joinWithStr, addToListInDict, getRows, SortedList


class IterablesTest(unittest.TestCase):
    def test_getIterable(self):
        self.assertEqual(getIterable(tuple()), [])
        self.assertEqual(getIterable([]), [])
        self.assertEqual(getIterable({}), [])
        self.assertEqual(getIterable(tuple([5, 2])), [5, 2])
        self.assertEqual(getIterable([5, 2]), [5, 2])
        self.assertEqual(getIterable({"a": 5, "b": 2}), [5, 2])

        self.assertFalse(getIterable(None))
        self.assertFalse(getIterable(5))
        self.assertFalse(getIterable("test"))
        self.assertFalse(getIterable(51.2))
        self.assertFalse(getIterable(True))

    def test_isIterable(self):
        self.assertTrue(isIterable(tuple()), [])
        self.assertTrue(isIterable([]), [])
        self.assertTrue(isIterable({}), [])
        self.assertTrue(isIterable(tuple([5, 2])), [5, 2])
        self.assertTrue(isIterable([5, 2]), [5, 2])
        self.assertTrue(isIterable({"a": 5, "b": 2}), [5, 2])

        self.assertFalse(isIterable(None))
        self.assertFalse(isIterable(5))
        self.assertFalse(isIterable("test"))
        self.assertFalse(isIterable(51.2))
        self.assertFalse(isIterable(True))

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

        self.assertEqual(joinWithStr(".", []), "")
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

    def test_getRows(self):
        self.assertEqual([[5]], getRows(5))
        self.assertEqual([[1, 2, 3]], getRows([1, 2, 3]))
        self.assertEqual([[1, 2, 3]], getRows([[1, 2, 3]]))
        self.assertEqual([[1, 2, 3]], getRows({1: [2, 3]}))

        self.assertEqual([[1, 2, 3], [4, 5, 6]], getRows({1: [2, 3], 4: [5, 6]}))
        self.assertEqual([[1, 2, 3], [4, 5, 6]], getRows([[1, 2, 3], [4, 5, 6]]))
        self.assertEqual([[1, 2, 3], [4, 5, 6]], getRows([{"a": 1,"b": 2,"c": 3}, {"d": 4, "e": 5, "f": 6}]))
        self.assertEqual([[1, 2, 3], [4, 5, 6]], getRows({1: {"b": 2, "c": 3}, 4: {"e": 5, "f": 6}}))

        self.assertEqual([], getRows([]))
        self.assertEqual([[], []], getRows([[], []]))
        self.assertEqual([], getRows(None))
        self.assertEqual([[0]], getRows(0))

    def test_SortedList(self):
        sortedList = SortedList(1, 2, 3)
        self.assertEqual([1, 2, 3], [obj for obj in sortedList])
        self.assertEqual([1, 2, 3], sortedList.objects)

        sortedList.add(2.5)
        self.assertEqual([1, 2, 2.5, 3], sortedList.objects)

        sortedList.add(0, 2)
        self.assertEqual([0, 1, 2, 2, 2.5, 3], sortedList.objects)

        sortedList.remove(2)
        self.assertEqual([0, 1, 2, 2.5, 3], sortedList.objects)

        sortedList.remove(2)
        self.assertEqual([0, 1, 2.5, 3], sortedList.objects)

        sortedList.remove(2)
        self.assertEqual([0, 1, 2.5, 3], sortedList.objects)

        sortedList.add(-1, 2)
        self.assertEqual([-1, 0, 1, 2, 2.5, 3], sortedList.objects)


        sortedList = SortedList("a", "aaa", "aa", getValueFunc=lambda obj: len(obj))
        self.assertEqual(["a", "aa", "aaa"], sortedList.objects)

        sortedList.add("aa")
        self.assertEqual(["a", "aa", "aa", "aaa"], sortedList.objects)




































