
import unittest

from generallibrary.iterables import getIterable, isIterable, depth, dictFirstValue, iterFirstValue, joinWithStr, addToListInDict, getRows, SortedList, appendToDict, addToDictInDict, getFreeIndex, exclusive, inclusive, uniqueObjInList, combine, remove_duplicates


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
        self.assertRaises(AssertionError, addToListInDict, None, "key", 5)
        self.assertRaises(AssertionError, addToListInDict, [], "key", 5)
        self.assertRaises(AssertionError, addToListInDict, {"key": "notlist"}, "key", 5)
        self.assertRaises(AssertionError, addToListInDict, {"key": {}}, "key", 5)

        d = {}
        self.assertEqual({"test": [5]}, addToListInDict(d, "test", 5))
        self.assertEqual({"test": [5, 3]}, addToListInDict(d, "test", 3))
        self.assertEqual({"test": [5, 3, 2, 0]}, addToListInDict(d, "test", 2, 0))
        self.assertEqual({"test": [5, 3, 2, 0, None, True]}, addToListInDict(d, "test", None, True))
        self.assertEqual({"test": [5, 3, 2, 0, None, True]}, d)

        self.assertEqual({"random": "foobar", True: [5, None, True, 2, "hi"]}, addToListInDict({"random": "foobar"}, True, 5, None, True, 2, "hi"))

    def test_addToDictInDict(self):
        self.assertRaises(AssertionError, addToDictInDict, None, "key", a=5)
        self.assertRaises(AssertionError, addToDictInDict, [], "key", a=5)
        self.assertRaises(AssertionError, addToDictInDict, {"key": "notdict"}, "key", a=5)
        self.assertRaises(AssertionError, addToDictInDict, {"key": []}, "key", a=5)

        d = {}
        self.assertEqual({"test": {"a": 5}}, addToDictInDict(d, "test", a=5))
        self.assertEqual({"test": {"a": 5, "b": 3}}, addToDictInDict(d, "test", b=3))
        self.assertEqual({"test": {"a": 5, "b": 3, "c": 2, "d": 0}}, addToDictInDict(d, "test", c=2, d=0))
        self.assertEqual({"test": {"a": 5, "b": 3, "c": 2, "d": 0, "e": None, "f": True}}, addToDictInDict(d, "test", e=None, f=True))
        self.assertEqual({"test": {"a": 5, "b": 3, "c": 2, "d": 0, "e": None, "f": True}}, d)

        self.assertEqual({"random": "foobar", True: {"b": 5, "c": None, "d": True, "e": 2, "f": "hi"}},
                         addToDictInDict({"random": "foobar"}, True, b=5, c=None, d=True, e=2, f="hi"))

    def test_getFreeIndex(self):
        d = {}
        self.assertEqual(0, getFreeIndex(d))

        d = {1: True}
        self.assertEqual(0, getFreeIndex(d))

        d[0] = True
        self.assertEqual(2, getFreeIndex(d))

        d[0.2] = True
        self.assertEqual(2, getFreeIndex(d))

        d[2.2] = True
        self.assertEqual(2, getFreeIndex(d))

        d["2"] = True
        self.assertEqual(2, getFreeIndex(d))

    def test_appendToDict(self):
        d = {}
        appendToDict(d, 5)
        self.assertEqual({0: 5}, d)

        appendToDict(d, "hello")
        self.assertEqual({0: 5, 1: "hello"}, d)

        appendToDict(d, 3.2)
        self.assertEqual({0: 5, 1: "hello", 2: 3.2}, d)

        del d[1]
        self.assertEqual({0: 5, 2: 3.2}, d)

        appendToDict(d, "hello")
        self.assertEqual({0: 5, 1: "hello", 2: 3.2}, d)

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

    def test_lusive(self):
        d = {"a": 5, "b": 3, "c": 4}
        self.assertEqual({'a': 5, 'c': 4}, exclusive(d, "b"))
        self.assertEqual({'c': 4}, exclusive(d, "a", "b"))
        self.assertEqual({}, exclusive(d, "a", "b", "c"))

        self.assertEqual({'b': 3}, inclusive(d, "b"))
        self.assertEqual({'a': 5, 'b': 3}, inclusive(d, "a", "b"))
        self.assertEqual({"a": 5, "b": 3, "c": 4}, inclusive(d, "a", "b", "c"))

    def test_uniqueObjInList(self):
        l = [5]
        self.assertEqual([5], l)

        uniqueObjInList(l, 5, True)
        self.assertEqual([5], l)

        uniqueObjInList(l, 5, False)
        self.assertEqual([], l)

        d = {"foo": "bar"}
        uniqueObjInList(l, d, False)
        self.assertEqual([], l)

        uniqueObjInList(l, d, True)
        self.assertEqual([d], l)

        uniqueObjInList(l, d, True)
        self.assertEqual([d], l)

        uniqueObjInList(l, 4, True)
        self.assertEqual([d, 4], l)

        uniqueObjInList(l, d, False)
        self.assertEqual([4], l)

        uniqueObjInList(l, 4, False)
        self.assertEqual([], l)

    def test_remove_duplicates(self):
        self.assertEqual([1, 2, 3], remove_duplicates([1, 1, 2, 3, 3]))
        self.assertEqual(["1", "2", "3"], remove_duplicates(["1", "1", "2", "3", "3"]))
        self.assertEqual(["hi", "there"], remove_duplicates(["hi", "there", "hi"]))
        self.assertEqual([(1, 2)], remove_duplicates([(1, 2), (1, 2)]))

        # self.assertEqual([{1: "foo", "bar": 5}], remove_duplicates([{1: "foo", "bar": 5}, {1: "foo", "bar": 5}]))

    def test_combine(self):
        self.assertEqual([{'a': 2, 'b': 4}, {'a': 2, 'b': 5}, {'a': 3, 'b': 4}, {'a': 3, 'b': 5}], combine(a=(2, 3), b=(4, 5)))
        self.assertEqual([{'a': 'hi', 'b': 4, 'c': [5]}, {'a': 'hi', 'b': None, 'c': [5]}], combine(a=("hi",), b=(4, None), c=([5],)))
        self.assertEqual([], combine())
        self.assertEqual([{"hello": None}], combine(hello=None))
        self.assertEqual([{"hello": 3, "there": 2}], combine(hello=3, there=2))
        self.assertEqual([{'hello': 3, 'there': 2}, {'hello': 3, 'there': "foobar"}], combine(hello=3, there=[2, "foobar"]))

    # def test_get_changes(self):
    #     self.assertEqual()
    #     {"hi": 5, "there": 4}
    #     {"hi": 7}





























