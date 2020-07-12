
import unittest

from generallibrary.functions import leadingArgsCount, getSignatureNames, getSignatureDefaults, changeArgsAndKwargs, getParameter


class FunctionsTest(unittest.TestCase):
    def test_leadingArgsCount(self):
        self.assertEqual(0, leadingArgsCount(lambda: 5))
        self.assertEqual(1, leadingArgsCount(lambda x: 5))
        self.assertEqual(2, leadingArgsCount(lambda x, y: 5))
        self.assertEqual(1, leadingArgsCount(lambda x, y=2: 5))
        self.assertEqual(0, leadingArgsCount(lambda x=3, y=2: 5))

        def hello(x, y, z=None):
            """2 args without default"""
            pass
        self.assertEqual(2, leadingArgsCount(hello))

        def hello(self, x, y=5, *args, **kwargs):
            """1 leading argument without a default value because self is ignored"""
            pass
        self.assertEqual(1, leadingArgsCount(hello))

        def hello(x, y, *args):
            """1 leading argument without a default value because self is ignored"""
            pass
        self.assertEqual(2, leadingArgsCount(hello))

    def test_getSignatureNames(self):
        self.assertEqual(None, getSignatureNames(5))
        self.assertEqual(None, getSignatureNames((5,).__init_subclass__))
        self.assertEqual([], getSignatureNames(lambda: 5))
        self.assertEqual(["x"], getSignatureNames(lambda x: 5))
        self.assertEqual(["x", "y"], getSignatureNames(lambda x, y: 5))
        self.assertEqual(["x", "y"], getSignatureNames(lambda x, y=2: 5))
        self.assertEqual(["x", "y"], getSignatureNames(lambda x=3, y=2: 5))

        def hello(x, y, z=None, *argz, **kwargz):
            """2 arg, 1 kwarg function"""
            pass
        self.assertEqual(["x", "y", "z", "argz", "kwargz"], getSignatureNames(hello))

    def test_getSignatureDefaults(self):
        self.assertEqual({"y": 5}, getSignatureDefaults(lambda x, y=5: None))
        self.assertEqual({"x": False, "y": 3.2}, getSignatureDefaults(lambda x=False, y=3.2: None))
        self.assertEqual({"x": False}, getSignatureDefaults(lambda x=False, *y: None))
        self.assertEqual({"y": None}, getSignatureDefaults(lambda x, y=None, *z: None))
        self.assertEqual({"y": None}, getSignatureDefaults(lambda x, y=None, **z: None))
        self.assertEqual({"y": "test"}, getSignatureDefaults(lambda x, y="test", *args, **z: None))

    def test_changeArgsAndKwargs(self):
        def wrapper(func):
            def f(*args, **kwargs):
                args, kwargs = changeArgsAndKwargs(func, args, kwargs, x=2)
                return func(*args, **kwargs)
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
                self.assertEqual(2, getParameter(func, args, kwargs, "x"))
                self.assertEqual(5, getParameter(func, args, kwargs, "y"))
                self.assertEqual(None, getParameter(func, args, kwargs, "z"))
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




































