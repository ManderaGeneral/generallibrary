
import unittest

from generallibrary.functions import SigInfo, defaults


class FunctionsTest(unittest.TestCase):
    def test_leadingArgNamesCount(self):
        self.assertEqual(0, len(SigInfo(lambda: 5).leadingArgNames))
        self.assertEqual(1, len(SigInfo(lambda x: 5).leadingArgNames))
        self.assertEqual(2, len(SigInfo(lambda x, y: 5).leadingArgNames))
        self.assertEqual(1, len(SigInfo(lambda x, y=2: 5).leadingArgNames))
        self.assertEqual(0, len(SigInfo(lambda x=3, y=2: 5).leadingArgNames))

        def hello(x, y, z=None):
            """2 args without default"""
            pass
        self.assertEqual(2, len(SigInfo(hello).leadingArgNames))

        def hello(self, x, y=5, *args, **kwargs):
            """1 leading argument without a default value because self is ignored"""
            pass
        self.assertEqual(1, len(SigInfo(hello).leadingArgNames))

        def hello(x, y, *args):
            """1 leading argument without a default value because self is ignored"""
            pass
        self.assertEqual(2, len(SigInfo(hello).leadingArgNames))

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

    def test_setParameters(self):
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

        sigInfo = SigInfo(lambda x, y, z=2: 5, (1, 2), {"z": 3})
        self.assertEqual(1, sigInfo["x"])
        self.assertEqual(2, sigInfo["y"])
        self.assertEqual(3, sigInfo["z"])
        self.assertEqual(None, sigInfo["doesntexist"])
        self.assertEqual([1, 2], sigInfo.args)
        self.assertEqual({"z": 3}, sigInfo.kwargs)

        sigInfo.setParameters(x=4, z=5)
        self.assertEqual(4, sigInfo["x"])
        self.assertEqual(2, sigInfo["y"])
        self.assertEqual(5, sigInfo["z"])
        self.assertEqual([4, 2], sigInfo.args)
        self.assertEqual({"z": 5}, sigInfo.kwargs)

        with self.assertRaises(AttributeError):
            sigInfo["new"] = 6

        sigInfo = SigInfo(lambda x=1, **kwargs: 5, kwargs={"y": 2})
        self.assertEqual(1, sigInfo["x"])
        self.assertEqual(2, sigInfo["y"])
        self.assertEqual([], sigInfo.args)
        self.assertEqual({"y": 2}, sigInfo.kwargs)

        sigInfo["y"] = 3
        self.assertEqual(3, sigInfo["y"])
        sigInfo["z"] = 4
        self.assertEqual(4, sigInfo["z"])
        sigInfo["x"] = 5
        self.assertEqual(5, sigInfo["x"])
        self.assertEqual({"x": 5, "y": 3, "z": 4}, sigInfo.kwargs)



    def test_getParameter(self):
        def wrapper(func):
            def f(*args, **kwargs):
                self.assertEqual(2, SigInfo(func, args, kwargs)["x"])
                self.assertEqual(5, SigInfo(func, args, kwargs)["y"])
                self.assertEqual(None, SigInfo(func, args, kwargs)["z"])
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

    def test_packedArgNames(self):
        self.assertEqual(["args"], SigInfo(lambda *args: 5).packedArgNames)
        self.assertEqual(["args"], SigInfo(lambda x, *args: 5).packedArgNames)
        self.assertEqual(["args"], SigInfo(lambda x, y=2, *args: 5).packedArgNames)
        self.assertEqual(["args"], SigInfo(lambda x, y=2, *args, **kwargs: 5).packedArgNames)

    def test_packedKwargNames(self):
        self.assertEqual(["kwargs"], SigInfo(lambda **kwargs: 5).packedKwargNames)
        self.assertEqual(["kwargs"], SigInfo(lambda x, **kwargs: 5).packedKwargNames)
        self.assertEqual(["kwargs"], SigInfo(lambda x, y=2, **kwargs: 5).packedKwargNames)
        self.assertEqual(["kwargs"], SigInfo(lambda x, y=2, *args, **kwargs: 5).packedKwargNames)

    def test_getIndexFromName(self):
        self.assertEqual(0, SigInfo(lambda x, y=2, *args, **kwargs: 5).getIndexFromName("x"))
        self.assertEqual(1, SigInfo(lambda x, y=2, *args, **kwargs: 5).getIndexFromName("y"))
        self.assertEqual(2, SigInfo(lambda x, y=2, *args, **kwargs: 5).getIndexFromName("args"))
        self.assertEqual(3, SigInfo(lambda x, y=2, *args, **kwargs: 5).getIndexFromName("kwargs"))

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
































