
import unittest

from generallibrary.functions import SigInfo, defaults


class FunctionsTest(unittest.TestCase):
    def test_leadingArgsCount(self):
        self.assertEqual(0, len(SigInfo(lambda: 5).leadingArgs))
        self.assertEqual(1, len(SigInfo(lambda x: 5).leadingArgs))
        self.assertEqual(2, len(SigInfo(lambda x, y: 5).leadingArgs))
        self.assertEqual(1, len(SigInfo(lambda x, y=2: 5).leadingArgs))
        self.assertEqual(0, len(SigInfo(lambda x=3, y=2: 5).leadingArgs))

        def hello(x, y, z=None):
            """2 args without default"""
            pass
        self.assertEqual(2, len(SigInfo(hello).leadingArgs))

        def hello(self, x, y=5, *args, **kwargs):
            """1 leading argument without a default value because self is ignored"""
            pass
        self.assertEqual(1, len(SigInfo(hello).leadingArgs))

        def hello(x, y, *args):
            """1 leading argument without a default value because self is ignored"""
            pass
        self.assertEqual(2, len(SigInfo(hello).leadingArgs))

    def test_getSignatureNames(self):
        self.assertRaises(AssertionError, SigInfo, 5)

        self.assertEqual([], SigInfo(lambda: 5).names)
        self.assertEqual(["x"], SigInfo(lambda x: 5).names)
        self.assertEqual(["x", "y"], SigInfo(lambda x, y: 5).names)
        self.assertEqual(["x", "y"], SigInfo(lambda x, y=2: 5).names)
        self.assertEqual(["x", "y"], SigInfo(lambda x=3, y=2: 5).names)

        self.assertEqual([], SigInfo(lambda x=3, y=2: 5).namesWithoutDefaults)
        self.assertEqual(["x"], SigInfo(lambda x, y=3: 5).namesWithoutDefaults)
        self.assertEqual(["x", "y"], SigInfo(lambda x, y: 5).namesWithoutDefaults)

        def hello(x, y, z=None, *argz, **kwargz):
            """2 arg, 1 kwarg function"""
            pass
        self.assertEqual(["x", "y", "z", "argz", "kwargz"], SigInfo(hello).names)

        self.assertEqual(["x", "y", "argz", "kwargz"], SigInfo(hello).namesWithoutDefaults)

    def test_getSignatureDefaults(self):
        self.assertEqual({"y": 5}, SigInfo(lambda x, y=5: None).defaults)
        self.assertEqual({"x": False, "y": 3.2}, SigInfo(lambda x=False, y=3.2: None).defaults)
        self.assertEqual({"x": False}, SigInfo(lambda x=False, *y: None).defaults)
        self.assertEqual({"y": None}, SigInfo(lambda x, y=None, *z: None).defaults)
        self.assertEqual({"y": None}, SigInfo(lambda x, y=None, **z: None).defaults)
        self.assertEqual({"y": "test"}, SigInfo(lambda x, y="test", *args, **z: None).defaults)

    def test_changeArgsAndKwargs(self):
        def wrapper(func):
            def f(*args, **kwargs):
                return SigInfo(func, args, kwargs).setParameters(x=2)()
            return f

        @wrapper
        def hello(x, y=5):
            return x * y

        self.assertEqual(10, hello(5))
        self.assertEqual(10, hello(x=5))
        self.assertEqual(4, hello(5, 2))
        self.assertEqual(4, hello(x=5, y=2))
        self.assertEqual(4, hello(5, y=2))

    def test_getParameter(self):
        def wrapper(func):
            def f(*args, **kwargs):
                self.assertEqual(2, SigInfo(func, args, kwargs).getParameter("x"))
                self.assertEqual(5, SigInfo(func, args, kwargs).getParameter("y"))
                self.assertEqual(None, SigInfo(func, args, kwargs).getParameter("z"))
                return func(*args, **kwargs)
            return f
        @wrapper
        def hello(x, y=5):
            return x * y
        hello(2)
        hello(x=2)
        hello(2, 5)
        hello(2, y=5)
        hello(x=2, y=5)

    def test_defaults(self):
        self.assertEqual({"a": 5, "b": 3}, defaults({"a": 5}, b=3))
        self.assertEqual({"a": 5, "b": 3}, defaults({"a": 5, "b": 3}, b=4))
        self.assertEqual({"a": 5, "b": 3}, defaults({"a": 5, "b": 3}, a=4))
        self.assertEqual({"a": 5, "b": 3}, defaults({"a": 5, "b": 3}, a=4, b=5))
        self.assertEqual({"a": 5, "b": 3}, defaults({}, a=5, b=3))


        self.assertEqual({"a": 5, "b": 3}, defaults({"a": 5, "b": 3}, a=4, b=5))
        self.assertEqual({"a": 5, "b": 3}, defaults({"a": 5, "b": 3}, a=4, b=5, overwriteNone=True))

        self.assertEqual({"a": 5, "b": 3}, defaults({"a": 5, "b": 3}, a=None, b=5))
        self.assertEqual({"a": 5, "b": 3}, defaults({"a": 5, "b": 3}, a=None, b=5, overwriteNone=True))

        self.assertEqual({"a": None, "b": 3}, defaults({"a": None, "b": 3}, a=4, b=5))
        self.assertEqual({"a": 4, "b": 3}, defaults({"a": None, "b": 3}, a=4, b=5, overwriteNone=True))


































