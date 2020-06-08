
import unittest

from generallibrary.functions import leadingArgsCount, getSignatureNames, changeArgsAndKwargs


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
        self.assertEqual(tuple(), getSignatureNames(lambda: 5))
        self.assertEqual(("x", ), getSignatureNames(lambda x: 5))
        self.assertEqual(("x", "y"), getSignatureNames(lambda x, y: 5))
        self.assertEqual(("x", "y"), getSignatureNames(lambda x, y=2: 5))
        self.assertEqual(("x", "y"), getSignatureNames(lambda x=3, y=2: 5))

        def hello(x, y, z=None, *argz, **kwargz):
            """2 arg, 1 kwarg function"""
            pass
        self.assertEqual(("x", "y", "z", "argz", "kwargz"), getSignatureNames(hello))

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





































