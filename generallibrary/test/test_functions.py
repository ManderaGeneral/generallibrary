
import unittest

from generallibrary import SigInfo, defaults, VerInfo, deco_cache, deco_cast_parameters, EmptyContext, deco_default_self_args


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

        self.assertEqual(["x"], SigInfo(lambda x, y=2: 5).leadingArgNames)
        self.assertEqual(["x"], SigInfo(lambda x, *argss, y=2: 5).leadingArgNames)
        self.assertEqual(["x", "z"], SigInfo(lambda x, z, *argss, y=2: 5).leadingArgNames)

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
        self.assertEqual(["x", "y"], SigInfo(hello).leadingArgNames)
        self.assertEqual(["x", "y", "argz", "kwargz"], SigInfo(hello).namesWithoutDefaults)
        self.assertEqual(["x", "y", "z"], SigInfo(hello).namesWithoutPacked)
        self.assertEqual("argz", SigInfo(hello).packedArgsName)
        self.assertEqual("kwargz", SigInfo(hello).packedKwargsName)

    def test_namesRequired(self):
        self.assertEqual(["x"], SigInfo(lambda x: 5).namesRequired)
        self.assertEqual(["x", "y"], SigInfo(lambda x, y: 5).namesRequired)
        self.assertEqual(["x"], SigInfo(lambda x, y=2: 5).namesRequired)
        self.assertEqual(["x"], SigInfo(lambda x, *y: 5).namesRequired)
        self.assertEqual(["x"], SigInfo(lambda x, z=2, *y: 5).namesRequired)
        self.assertEqual(["x"], SigInfo(lambda x, **y: 5).namesRequired)
        self.assertEqual(["x"], SigInfo(lambda x, **y: 5).namesRequired)

    def test_argNames(self):
        sigInfo = SigInfo(lambda x, y=2, b=4, *args, z=3, s, **kwargs: 5)
        self.assertEqual(["x", "y", "b", "args"], sigInfo.positionalArgNames)
        self.assertEqual(["z", "s", "kwargs"], sigInfo.keywordArgNames)
        self.assertEqual({"y": 2, "b": 4, "z": 3}, sigInfo.defaults)

    def test_getSignatureDefaults(self):
        self.assertEqual({"y": 5}, SigInfo(lambda x, y=5: None).defaults)
        self.assertEqual({"x": False, "y": 3.2}, SigInfo(lambda x=False, y=3.2: None).defaults)
        self.assertEqual({"x": False}, SigInfo(lambda x=False, *y: None).defaults)
        self.assertEqual({"y": None}, SigInfo(lambda x, y=None, *z: None).defaults)
        self.assertEqual({"y": None}, SigInfo(lambda x, y=None, **z: None).defaults)
        self.assertEqual({"y": "test"}, SigInfo(lambda x, y="test", *args, **z: None).defaults)

    def test_setParameters(self):
        def _wrapper(func):
            def _f(*args, **kwargs):
                return SigInfo(func, *args, **kwargs).setParameters(x=2)()
            return _f

        @_wrapper
        def _hello(x, y=5):
            return x * y

        self.assertEqual(10, _hello(5))
        self.assertEqual(10, _hello(x=5))
        self.assertEqual(4, _hello(5, 2))
        self.assertEqual(4, _hello(x=5, y=2))
        self.assertEqual(4, _hello(5, y=2))

        sigInfo = SigInfo(lambda x, y, z=2: 5, 1, 2, z=3)
        self.assertEqual(1, sigInfo["x"])
        self.assertEqual(2, sigInfo["y"])
        self.assertEqual(3, sigInfo["z"])
        self.assertEqual(None, sigInfo["doesntexist"])
        self.assertEqual([1, 2, 3], sigInfo.unpackedArgs)
        self.assertEqual({}, sigInfo.unpackedKwargs)

        sigInfo.setParameters(x=4, z=5)
        self.assertEqual(4, sigInfo["x"])
        self.assertEqual(2, sigInfo["y"])
        self.assertEqual(5, sigInfo["z"])
        self.assertEqual([4, 2, 5], sigInfo.unpackedArgs)
        self.assertEqual({}, sigInfo.unpackedKwargs)

        # with self.assertRaises(AssertionError):
        #     sigInfo["new"] = 6
        sigInfo["new"] = 6

        sigInfo = SigInfo(lambda x=1, **kwargs: 5, y=2)
        self.assertEqual(1, sigInfo["x"])
        self.assertEqual(2, sigInfo["y"])
        self.assertEqual([1], sigInfo.unpackedArgs)
        self.assertEqual({"y": 2}, sigInfo.unpackedKwargs)

        sigInfo["y"] = 3
        self.assertEqual(3, sigInfo["y"])
        sigInfo["z"] = 4
        self.assertEqual(4, sigInfo["z"])
        sigInfo["x"] = 5
        self.assertEqual(5, sigInfo["x"])
        self.assertEqual([5], sigInfo.unpackedArgs)
        self.assertEqual({"y": 3, "z": 4}, sigInfo.unpackedKwargs)



    def test_getParameter(self):
        def _wrapper(func):
            def _f(*args, **kwargs):
                self.assertEqual(2, SigInfo(func, *args, **kwargs)["x"])
                self.assertEqual(5, SigInfo(func, *args, **kwargs)["y"])
                self.assertEqual(None, SigInfo(func, *args, **kwargs)["z"])
                return func(*args, **kwargs)
            return _f
        @_wrapper
        def _hello(x, y=5):
            return x * y
        _hello(2)
        _hello(x=2)
        _hello(2, 5)
        _hello(2, y=5)
        _hello(x=2, y=5)

    def test_packedArgs(self):
        self.assertEqual("args", SigInfo(lambda *args: 5).packedArgsName)
        self.assertEqual("args", SigInfo(lambda x, *args: 5).packedArgsName)
        self.assertEqual("args", SigInfo(lambda x, y=2, *args: 5).packedArgsName)
        self.assertEqual("args", SigInfo(lambda x, y=2, *args, **kwargs: 5).packedArgsName)

    def test_packedKwargNames(self):
        self.assertEqual("kwargs", SigInfo(lambda **kwargs: 5).packedKwargsName)
        self.assertEqual("kwargs", SigInfo(lambda x, **kwargs: 5).packedKwargsName)
        self.assertEqual("kwargs", SigInfo(lambda x, y=2, **kwargs: 5).packedKwargsName)
        self.assertEqual("kwargs", SigInfo(lambda x, y=2, *args, **kwargs: 5).packedKwargsName)

    def test_getIndexFromName(self):
        self.assertEqual(0, SigInfo(lambda x, y=2, *args, **kwargs: 5).getIndexFromName("x"))
        self.assertEqual(1, SigInfo(lambda x, y=2, *args, **kwargs: 5).getIndexFromName("y"))
        self.assertEqual(2, SigInfo(lambda x, y=2, *args, **kwargs: 5).getIndexFromName("args"))
        self.assertEqual(3, SigInfo(lambda x, y=2, *args, **kwargs: 5).getIndexFromName("kwargs"))

    def test_sigInfo(self):
        self.assertEqual([1, 2], SigInfo(lambda *arguments: 5, 1, 2)["arguments"])
        self.assertEqual([2], SigInfo(lambda x, *arguments: 5, 1, 2)["arguments"])

        self.assertEqual({"foo": "bar", "test": 5}, SigInfo(lambda x, *arguments, **keywordargs: 5, 1, 2, foo="bar", test=5)["keywordargs"])

        sigInfo = SigInfo(lambda x, y=6, *arguments, z=7, **keywordargs: 8, 1, 2, 3, 4, foo="bar", test=5)
        self.assertEqual(1, sigInfo["x"])
        self.assertEqual(2, sigInfo["y"])
        self.assertEqual([3, 4], sigInfo["arguments"])
        self.assertEqual(7, sigInfo["z"])
        self.assertEqual({"foo": "bar", "test": 5}, sigInfo["keywordargs"])

        sigInfo = SigInfo(lambda x, **kwargs: 3, 1, x=2)
        self.assertEqual(1, sigInfo["x"])

    def test_definedNames(self):
        self.assertEqual(["y", "a"], SigInfo(lambda x, y=2, *args, z, a=3, **kwargs: 5).definedNames)
        self.assertEqual(["x", "y", "a"], SigInfo(lambda x, y=2, *args, z, a=3, **kwargs: 5, 1).definedNames)
        self.assertEqual(["x", "y", "a"], SigInfo(lambda x, y=2, *args, z, a=3, **kwargs: 5, 1, 2).definedNames)
        self.assertEqual(["x", "y", "args", "a"], SigInfo(lambda x, y=2, *args, z, a=3, **kwargs: 5, 1, 2, 3).definedNames)
        self.assertEqual(["x", "y", "args", "a", "kwargs"], SigInfo(lambda x, y=2, *args, z, a=3, **kwargs: 5, 1, 2, 3, b=4).definedNames)

    def test_validParameters(self):
        self.assertEqual(False, SigInfo(lambda x, y=2, *args, z, a=3, **kwargs: 5).requiredAreDefined)
        self.assertEqual(False, SigInfo(lambda x, y=2, *args, z, a=3, **kwargs: 5, 1).requiredAreDefined)
        self.assertEqual(False, SigInfo(lambda x, y=2, *args, z, a=3, **kwargs: 5, 1, 2).requiredAreDefined)
        self.assertEqual(False, SigInfo(lambda x, y=2, *args, z, a=3, **kwargs: 5, 1, 2, 3).requiredAreDefined)
        self.assertEqual(False, SigInfo(lambda x, y=2, *args, z, a=3, **kwargs: 5, 1, 2, 3, 4).requiredAreDefined)
        self.assertEqual(True, SigInfo(lambda x, y=2, *args, z, a=3, **kwargs: 5, 1, 2, 3, z=5).requiredAreDefined)
        self.assertEqual(False, SigInfo(lambda x, y=2, *args, z, a=3, **kwargs: 5, 1, 2, 3, a=5).requiredAreDefined)
        self.assertEqual(True, SigInfo(lambda x, y=2, *args, z, a=3, **kwargs: 5, 1, 2, 3, a=5, z=6).requiredAreDefined)

    def test_sigInfoCall(self):
        sigInfo = SigInfo(lambda x: x, 5)
        self.assertEqual(5, sigInfo())

        sigInfo["x"] = 3
        self.assertEqual(3, sigInfo())

        sigInfo["new"] = 4
        self.assertEqual(3, sigInfo())

        sigInfo = SigInfo(lambda x: x)
        self.assertRaises(AssertionError, sigInfo)

        sigInfo["x"] = 3
        self.assertEqual(3, sigInfo())

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

    def test_unpackedAllArgs_without_missing(self):
        class _Foo:
            @deco_default_self_args
            def _bar(self, req):
                return req
        foo = _Foo()
        self.assertRaises(AttributeError, _Foo()._bar)

        setattr(foo, "req", None)
        self.assertEqual(None, foo._bar())

        setattr(foo, "req", "test")
        self.assertEqual("test", foo._bar())

        self.assertEqual("hello", foo._bar(req="hello"))


        class _Foo:
            def __init__(self):
                self.random = 4
                self._req = 2

            @deco_default_self_args
            def _bar(self, random, *args, _req, extra=2):
                return random, _req

        self.assertEqual((4, 2), _Foo()._bar())

        self.assertEqual((5, 2), _Foo()._bar(random=5))
        self.assertEqual((4, 3), _Foo()._bar(_req=3))
        self.assertEqual((6, 7), _Foo()._bar(random=6, _req=7))
        self.assertEqual((8, 2), _Foo()._bar(8, 9, 10, 11))


    # Not happy about this technique to dynamically load code to prevent syntax error, but it's the best option so far
    @unittest.skipUnless(VerInfo().positionalArgument, "Positional-only parameters were introduced in 3.8.0.")
    def test_positional(self):
        from generallibrary.test.positional import positional
        positional(self)

    def test_deco_cache(self):
        import time

        @deco_cache()
        def _test():
            time.sleep(0.2)
            return "foo"

        start_time = time.time()
        _test()
        self.assertGreaterEqual(time.time() - start_time, 0.19)
        _test()
        self.assertLess(time.time() - start_time, 0.39)

    def test_deco_cast_parameters(self):
        @deco_cast_parameters(x=int)
        def test(x):
            return x
        self.assertEqual(True, isinstance(test("2"), int))


    def test_EmptyContext(self):
        with EmptyContext():
            pass







































































