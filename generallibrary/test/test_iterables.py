
from generallibrary.iterables import *

import unittest


class IterablesTest(unittest.TestCase):
    def test_get_keys(self):
        self.assertEqual([0, 1, 2], list(get_keys([1, 2, 3])))
        self.assertEqual([0, 1, 2], list(get_keys((1, 2, 3))))
        self.assertEqual([0, 1, 2], list(get_keys({1, 2, 3})))
        self.assertEqual(["a", "b", "c"], list(get_keys({"a": 1, "b": 2, "c": 3})))

    def test_get_values(self):
        self.assertEqual([1, 2, 3], list(get_values([1, 2, 3])))
        self.assertEqual([1, 2, 3], list(get_values((1, 2, 3))))
        self.assertEqual({1, 2, 3}, set(get_values({1, 2, 3})))
        self.assertEqual([1, 2, 3], list(get_values({"a": 1, "b": 2, "c": 3})))

    def test_get_items(self):
        self.assertEqual({0: 1, 1: 2, 2: 3}, dict(get_items([1, 2, 3])))
        self.assertEqual({0: 1, 1: 2, 2: 3}, dict(get_items((1, 2, 3))))
        self.assertEqual(3, len(dict(get_items({1, 2, 3}))))
        self.assertEqual({"a": 1, "b": 2, "c": 3}, dict(get_items({"a": 1, "b": 2, "c": 3})))

    def test_is_iterable(self):
        self.assertTrue(is_iterable(tuple()))
        self.assertTrue(is_iterable([]))
        self.assertTrue(is_iterable({}))
        self.assertTrue(is_iterable(tuple([5, 2])))
        self.assertTrue(is_iterable([5, 2]))
        self.assertTrue(is_iterable({"a": 5, "b": 2}))
        self.assertTrue(is_iterable("test"))

        self.assertFalse(is_iterable(None))
        self.assertFalse(is_iterable(5))
        self.assertFalse(is_iterable(51.2))
        self.assertFalse(is_iterable(True))
        self.assertFalse(is_iterable(Ellipsis))

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

    def test_iter_first_value(self):
        self.assertEqual(None, iter_first_value({}))

        self.assertEqual(iter_first_value({"a": 5}), 5)
        self.assertEqual(iter_first_value({"a": 5, "b": 5}), 5)

        self.assertIsNone(iter_first_value([]))
        self.assertEqual(iter_first_value([5]), 5)
        self.assertEqual(iter_first_value([5, 2, 3]), 5)

        self.assertIsNone(iter_first_value(tuple()))
        self.assertEqual(iter_first_value(tuple([5])), 5)
        self.assertEqual(iter_first_value(tuple([5, 2, 3])), 5)

    def test_join_with_str(self):
        self.assertRaises(Exception, join_with_str, ".", 5)

        self.assertEqual(join_with_str(".", "abc"), "a.b.c")
        self.assertEqual(join_with_str(".", [1, 2, 3]), "1.2.3")
        self.assertEqual(join_with_str(".", {"a": 1, "b": 2, "c": 3}), "1.2.3")
        self.assertEqual(join_with_str(".", {"a": "1", "b": 2, "c": 3}), "1.2.3")
        self.assertEqual(join_with_str(".", tuple([1, 2, 3])), "1.2.3")
        self.assertEqual(join_with_str(".", [["foo", "bar"]]), "['foo', 'bar']")
        self.assertEqual(join_with_str(".", [["foo", "bar"], ["foo", "bar"]]), "['foo', 'bar'].['foo', 'bar']")

    def test_extend_list_in_dict(self):
        self.assertRaises(AssertionError, extend_list_in_dict, None, "key", 5)
        self.assertRaises(AssertionError, extend_list_in_dict, [], "key", 5)
        self.assertRaises(AssertionError, extend_list_in_dict, {"key": "notlist"}, "key", 5)
        self.assertRaises(AssertionError, extend_list_in_dict, {"key": {}}, "key", 5)

        d = {}
        self.assertEqual({"test": [5]}, extend_list_in_dict(d, "test", 5))
        self.assertEqual({"test": [5, 3]}, extend_list_in_dict(d, "test", 3))
        self.assertEqual({"test": [5, 3, 2, 0]}, extend_list_in_dict(d, "test", 2, 0))
        self.assertEqual({"test": [5, 3, 2, 0, None, True]}, extend_list_in_dict(d, "test", None, True))
        self.assertEqual({"test": [5, 3, 2, 0, None, True]}, d)

        self.assertEqual({"random": "foobar", True: [5, None, True, 2, "hi"]}, extend_list_in_dict({"random": "foobar"}, True, 5, None, True, 2, "hi"))

    def test_update_dict_in_dict(self):
        self.assertRaises(AssertionError, update_dict_in_dict, None, "key", a=5)
        self.assertRaises(AssertionError, update_dict_in_dict, [], "key", a=5)
        self.assertRaises(AssertionError, update_dict_in_dict, {"key": "notdict"}, "key", a=5)
        self.assertRaises(AssertionError, update_dict_in_dict, {"key": []}, "key", a=5)

        d = {}
        self.assertEqual({"test": {"a": 5}}, update_dict_in_dict(d, "test", a=5))
        self.assertEqual({"test": {"a": 5, "b": 3}}, update_dict_in_dict(d, "test", b=3))
        self.assertEqual({"test": {"a": 5, "b": 3, "c": 2, "d": 0}}, update_dict_in_dict(d, "test", c=2, d=0))
        self.assertEqual({"test": {"a": 5, "b": 3, "c": 2, "d": 0, "e": None, "f": True}}, update_dict_in_dict(d, "test", e=None, f=True))
        self.assertEqual({"test": {"a": 5, "b": 3, "c": 2, "d": 0, "e": None, "f": True}}, d)

        self.assertEqual({"random": "foobar", True: {"b": 5, "c": None, "d": True, "e": 2, "f": "hi"}},
                         update_dict_in_dict({"random": "foobar"}, True, b=5, c=None, d=True, e=2, f="hi"))

    def test_get_free_index(self):
        d = {}
        self.assertEqual(0, get_free_index(d))

        d = {1: True}
        self.assertEqual(0, get_free_index(d))

        d[0] = True
        self.assertEqual(2, get_free_index(d))

        d[0.2] = True
        self.assertEqual(2, get_free_index(d))

        d[2.2] = True
        self.assertEqual(2, get_free_index(d))

        d["2"] = True
        self.assertEqual(2, get_free_index(d))

    def test_append_to_dict(self):
        d = {}
        append_to_dict(d, 5)
        self.assertEqual({0: 5}, d)

        append_to_dict(d, "hello")
        self.assertEqual({0: 5, 1: "hello"}, d)

        append_to_dict(d, 3.2)
        self.assertEqual({0: 5, 1: "hello", 2: 3.2}, d)

        del d[1]
        self.assertEqual({0: 5, 2: 3.2}, d)

        append_to_dict(d, "hello")
        self.assertEqual({0: 5, 1: "hello", 2: 3.2}, d)

    def test_get_rows(self):
        self.assertEqual([[5]], get_rows(5))
        self.assertEqual([[1, 2, 3]], get_rows([1, 2, 3]))
        self.assertEqual([[1, 2, 3]], get_rows([[1, 2, 3]]))
        self.assertEqual([[1, 2, 3]], get_rows({1: [2, 3]}))

        self.assertEqual([[1, 2, 3], [4, 5, 6]], get_rows({1: [2, 3], 4: [5, 6]}))
        self.assertEqual([[1, 2, 3], [4, 5, 6]], get_rows([[1, 2, 3], [4, 5, 6]]))
        self.assertEqual([[1, 2, 3], [4, 5, 6]], get_rows([{"a": 1,"b": 2,"c": 3}, {"d": 4, "e": 5, "f": 6}]))
        self.assertEqual([[1, 2, 3], [4, 5, 6]], get_rows({1: {"b": 2, "c": 3}, 4: {"e": 5, "f": 6}}))

        self.assertEqual([], get_rows([]))
        self.assertEqual([[], []], get_rows([[], []]))
        self.assertEqual([], get_rows(None))
        self.assertEqual([[0]], get_rows(0))

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

    def test_unique_obj_in_list(self):
        l = [5]
        self.assertEqual([5], l)

        unique_obj_in_list(l, 5, True)
        self.assertEqual([5], l)

        unique_obj_in_list(l, 5, False)
        self.assertEqual([], l)

        d = {"foo": "bar"}
        unique_obj_in_list(l, d, False)
        self.assertEqual([], l)

        unique_obj_in_list(l, d, True)
        self.assertEqual([d], l)

        unique_obj_in_list(l, d, True)
        self.assertEqual([d], l)

        unique_obj_in_list(l, 4, True)
        self.assertEqual([d, 4], l)

        unique_obj_in_list(l, d, False)
        self.assertEqual([4], l)

        unique_obj_in_list(l, 4, False)
        self.assertEqual([], l)

    def test_remove_duplicates(self):
        self.assertEqual([1, 2, 3], remove_duplicates([1, 1, 2, 3, 3]))
        self.assertEqual(["1", "2", "3"], remove_duplicates(["1", "1", "2", "3", "3"]))
        self.assertEqual(["hi", "there"], remove_duplicates(["hi", "there", "hi"]))
        self.assertEqual([(1, 2)], remove_duplicates([(1, 2), (1, 2)]))

        self.assertEqual([1.1, 1.6], remove_duplicates([0.9, 1, 1.1, 1.6], func=round))
        # self.assertEqual([{1: "foo", "bar": 5}], remove_duplicates([{1: "foo", "bar": 5}, {1: "foo", "bar": 5}]))

    def test_combine(self):
        self.assertEqual([{'a': 2, 'b': 4}, {'a': 2, 'b': 5}, {'a': 3, 'b': 4}, {'a': 3, 'b': 5}], combine(a=(2, 3), b=(4, 5)))
        self.assertEqual([{'a': 'hi', 'b': 4, 'c': [5]}, {'a': 'hi', 'b': None, 'c': [5]}], combine(a=("hi",), b=(4, None), c=([5],)))
        self.assertEqual([], combine())
        self.assertEqual([{"hello": None}], combine(hello=None))
        self.assertEqual([{"hello": 3, "there": 2}], combine(hello=3, there=2))
        self.assertEqual([{'hello': 3, 'there': 2}, {'hello': 3, 'there': "foobar"}], combine(hello=3, there=[2, "foobar"]))

    def test_get_index(self):
        self.assertEqual("a", get_index({"a": 2, "b": 4}, 2))
        self.assertEqual("b", get_index({"a": 2, "b": 4}, 4))
        self.assertEqual(None, get_index({"a": 2, "b": 4}, 3, None))
        self.assertRaises(ValueError, lambda: get_index({"a": 2, "b": 4}, 3))

    def test_pivot_list(self):
        l = [1, 2, 3]
        self.assertEqual([3, 1, 2], pivot_list(l, -4))
        self.assertEqual([1, 2, 3], pivot_list(l, -3))
        self.assertEqual([2, 3, 1], pivot_list(l, -2))
        self.assertEqual([3, 1, 2], pivot_list(l, -1))
        self.assertEqual([1, 2, 3], pivot_list(l, 0))
        self.assertEqual([2, 3, 1], pivot_list(l, 1))
        self.assertEqual([3, 1, 2], pivot_list(l, 2))
        self.assertEqual([1, 2, 3], pivot_list(l, 3))
        self.assertEqual([2, 3, 1], pivot_list(l, 4))

    def test_split_list(self):
        l = [1, 2, 3]
        self.assertEqual(([1], [2, 3]), split_list(lambda x: x < 2, *l))
        self.assertEqual(([1, 3], [2]), split_list(lambda x: x != 2, *l))

    def test_remove_dict(self):
        a = {"a": "b", 5: "c"}
        self.assertEqual(True, remove(a, "b"))
        self.assertEqual({5: "c"}, a)
        self.assertEqual(False, remove(a, "b"))
        self.assertEqual({5: "c"}, a)

        self.assertEqual(True, remove(a, "c"))
        self.assertEqual({}, a)
        self.assertEqual(False, remove(a, "c"))

    def test_remove_list(self):
        a = ["a", "b", 5]
        self.assertEqual(True, remove(a, "b"))
        self.assertEqual(["a", 5], a)
        self.assertEqual(False, remove(a, "b"))

    def test_remove_set(self):
        a = {"a", "b", 5}
        self.assertEqual(True, remove(a, "b"))
        self.assertEqual({"a", 5}, a)
        self.assertEqual(False, remove(a, "b"))

    def test_flatten(self):
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], flatten(a))

    def test_subtract_list(self):
        self.assertEqual([1], subtract_list([1, 2], [2]))
        self.assertEqual([1], subtract_list([1, 1], [1]))
        self.assertEqual([], subtract_list([1, 1], [1, 1]))
        self.assertEqual([False], subtract_list([False, True, None], [None, True]))

    def test_dict_insert(self):
        x = {"b": 2}
        dict_insert(x, a=1)
        self.assertEqual(["a", "b"], list(x.keys()))
        x["c"] = 3
        self.assertEqual(["a", "b", "c"], list(x.keys()))
        dict_insert(x, d=4, e=5)
        self.assertEqual(["d", "e", "a", "b", "c"], list(x.keys()))




















