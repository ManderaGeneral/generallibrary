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

            @deco_require(lambda self: self.x == 5, lambda func: f"{func.__name__} failed")
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
