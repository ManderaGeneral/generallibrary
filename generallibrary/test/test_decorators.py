from generallibrary.decorators import deco_require, SigInfo

import unittest


class DecoratorsTest(unittest.TestCase):
    def test_deco_require_simple(self):
        class X:
            def __init__(self, x):
                self.x = x

            @deco_require(lambda self: self.x == 5)
            def foo(self):
                return self.x

        self.assertEqual(5, X(5).foo())
        self.assertRaises(AssertionError, X(2).foo)

    def test_deco_require_message(self):
        class X:
            def __init__(self, x):
                self.x = x

            @deco_require(lambda self: self.x == 5, message=lambda func: f"{func.__name__} failed")
            def foo(self):
                return self.x

        self.assertEqual(5, X(5).foo())
        self.assertRaises(AssertionError, X(2).foo)

        self.assertRaisesRegex(AssertionError, "foo failed", X(2).foo)

    def test_deco_require_no_lambda(self):
        class X:
            def __init__(self, x):
                self.x = x

            def check(self) -> bool:
                return self.x == 5

            @deco_require(check)
            def foo(self):
                return self.x

        self.assertEqual(5, X(5).foo())
        self.assertRaises(AssertionError, X(2).foo)

        self.assertRaisesRegex(AssertionError, "'foo' requires 'check' function to be True.", X(2).foo)

    def test_deco_require_function(self):
        def check():
            return True

        @deco_require(check)
        def x():
            return 5

        self.assertEqual(5, x())

    def test_deco_require_non_callable(self):
        @deco_require(True)
        def x():
            return 5

        self.assertEqual(5, x())

    def test_deco_require_non_callable_false(self):
        @deco_require(False)
        def x():
            return 5

        self.assertRaises(AssertionError, x)

    def test_deco_require_args(self):
        def check(val):
            return val == 3

        @deco_require(check, 3)
        def x():
            return 5

        self.assertEqual(5, x())

    def test_deco_require_args_false(self):
        def check(val):
            return val == 3

        @deco_require(check, 4)
        def x():
            return 5

        self.assertRaises(AssertionError, x)

    def test_deco_require_kwargs(self):
        def check(val):
            return val == 3

        @deco_require(check, val=3)
        def x():
            return 5

        self.assertEqual(5, x())

    def test_deco_require_kwargs_false(self):
        def check(val):
            return val == 3

        @deco_require(check, val=4)
        def x():
            return 5

        self.assertRaises(AssertionError, x)

    def test_deco_require_args_and_kwargs(self):
        def check(a, b):
            return a == 2 and b == 3

        @deco_require(check, 2, b=3)
        def x():
            return 5

        self.assertEqual(5, x())

    def test_deco_require_args_and_kwargs_false(self):
        def check(a, b):
            return a == 2 and b == 3

        @deco_require(check, 3, b=4)
        def x():
            return 5

        self.assertRaises(AssertionError, x)

    def test_deco_require_args_from_func(self):
        def check(val):
            return val == 3

        @deco_require(check)
        def x(val):
            return 5

        self.assertEqual(5, x(3))
        self.assertEqual(5, x(val=3))
        self.assertRaises(AssertionError, x, 4)
        self.assertRaises(AssertionError, x, val=4)

    def test_deco_require_args_from_func_combined(self):
        def check(val2, val):
            return val == 3 and val2 == 4

        @deco_require(check, 4)
        def x(val):
            return 5

        self.assertEqual(5, x(3))
        self.assertEqual(5, x(val=3))
        self.assertRaises(AssertionError, x, 4)
        self.assertRaises(AssertionError, x, val=4)


    def test_siginfo_custom_parameters_int(self):
        self.assertEqual(0, SigInfo(int).call())
        self.assertEqual(5, SigInfo(int, 5).call())
        self.assertEqual(5, SigInfo(int, "5").call())

    def test_siginfo_custom_parameters_str(self):
        self.assertEqual("", SigInfo(str).call())
        self.assertEqual("5", SigInfo(str, 5).call())
        self.assertEqual("hii", SigInfo(str, "hii").call())

    def test_siginfo_custom_parameters_bool(self):
        self.assertEqual(False, SigInfo(bool).call())
        self.assertEqual(True, SigInfo(bool, 5).call())
        self.assertEqual(False, SigInfo(bool, None).call())

    def test_siginfo_custom_parameters_dict(self):
        self.assertEqual({}, SigInfo(dict).call())
        self.assertEqual({"hi": "there", "yo": 5}, SigInfo(dict, [["hi", "there"]], yo=5).call())
        self.assertEqual({"a": "b"}, SigInfo(dict, ["ab"]).call())
        self.assertEqual({"a": "b"}, SigInfo(dict, {"a": "b"}).call())
