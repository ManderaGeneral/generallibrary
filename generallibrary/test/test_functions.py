
from generallibrary.functions import *
from generallibrary import VerInfo, cache_clear, TreeDiagram

import unittest


def _orphan():
    pass


class FunctionsTest(unittest.TestCase):
    def test_classproperty(self):
        class Foo:
            x = 5

            def __init__(self):
                self.x = 3

            @classproperty
            def bar(cls):
                return cls.x

        self.assertEqual(5, Foo.bar)
        self.assertEqual(5, Foo().bar)

        self.assertEqual(5, Foo.x)
        self.assertEqual(3, Foo().x)

    def test_deco_bound_defaults(self):
        class A:
            x = 1

            def __init__(self):
                self.y = 2

            @deco_bound_defaults
            def foo(self, x, y, z=3):
                return x, y, z

        self.assertEqual((1, 2, 3), A().foo())

    def test_class_from_callable(self):
        self.assertEqual(FunctionsTest, SigInfo(lambda: None).class_from_callable())
        self.assertEqual(FunctionsTest, SigInfo(FunctionsTest.test_class_from_callable).class_from_callable())
        self.assertEqual(None, SigInfo(_orphan).class_from_callable())
        self.assertEqual(None, SigInfo(FunctionsTest).class_from_callable())

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
        self.assertEqual(["x", "y"], SigInfo(lambda x=3, y=2: 5).positional_extra)

        self.assertEqual([], SigInfo(lambda x=3, y=2: 5).namesWithoutDefaults)
        self.assertEqual(["x"], SigInfo(lambda x, y=3: 5).namesWithoutDefaults)
        self.assertEqual(["x", "y"], SigInfo(lambda x, y: 5).namesWithoutDefaults)

        def hello(x, y, z=None, *argz, **kwargz):
            """2 arg, 1 kwarg function"""
            pass
        self.assertEqual(["x", "y", "z"], SigInfo(hello).positional_extra)
        self.assertEqual(["x", "y", "z", "argz", "kwargz"], SigInfo(hello).names)
        self.assertEqual(["x", "y"], SigInfo(hello).leadingArgNames)
        self.assertEqual(["x", "y", "argz", "kwargz"], SigInfo(hello).namesWithoutDefaults)
        self.assertEqual(["x", "y", "z"], SigInfo(hello).namesWithoutPacked)
        self.assertEqual("argz", SigInfo(hello).packedArgsName)
        self.assertEqual("kwargz", SigInfo(hello).packedKwargsName)

        class _Foo:
            def __init__(self, x, y):
                pass

            @classmethod
            def _bar(cls):
                pass

        self.assertEqual([], SigInfo(_Foo._bar).names)
        self.assertEqual(["cls"], SigInfo(_Foo._bar).positional_extra)

        self.assertEqual(_Foo._bar, SigInfo(_Foo._bar).callableObject)

        self.assertEqual(["x", "y"], SigInfo(_Foo).names)
        self.assertEqual({"x": 1, "y": 2}, SigInfo(_Foo, 1, 2).allArgs)
        self.assertEqual({"x": 1, "y": 2}, SigInfo(_Foo, 1, y=2).allArgs)
        self.assertEqual({"x": 1, "y": 2}, SigInfo(_Foo, x=1, y=2).allArgs)

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
        self.assertEqual(["z", "s", "kwargs"], sigInfo.positionalOppositeArgNames)
        self.assertEqual({"y": 2, "b": 4, "z": 3}, sigInfo.defaults)

    def test_getSignatureDefaults(self):
        self.assertEqual({}, SigInfo(lambda: None).defaults)
        self.assertEqual({"y": 5}, SigInfo(lambda x, y=5: None).defaults)
        self.assertEqual({"x": False, "y": 3.2}, SigInfo(lambda x=False, y=3.2: None).defaults)
        self.assertEqual({"x": False}, SigInfo(lambda x=False, *y: None).defaults)
        self.assertEqual({"y": None}, SigInfo(lambda x, y=None, *z: None).defaults)
        self.assertEqual({"y": None}, SigInfo(lambda x, y=None, **z: None).defaults)
        self.assertEqual({"y": "test"}, SigInfo(lambda x, y="test", *args, **z: None).defaults)

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

        self.assertEqual({"foo": "bar", "test": 5}, SigInfo(lambda x, *arguments, **keywordargs: None, 1, 2, foo="bar", test=5).packedKwargs)

        sigInfo = SigInfo(lambda x, y=6, *arguments, z=7, **keywordargs: None, 1, 2, 3, 4, foo="bar", test=5)
        self.assertEqual(1, sigInfo["x"])
        self.assertEqual(2, sigInfo["y"])
        self.assertEqual([3, 4], sigInfo["arguments"])
        self.assertEqual(7, sigInfo["z"])
        self.assertEqual({"foo": "bar", "test": 5}, sigInfo.packedKwargs)

        self.assertEqual([1, 2, 3, 4], sigInfo.unpackedArgs)
        self.assertEqual({"z": 7, "foo": "bar", "test": 5}, sigInfo.unpackedKwargs)

        sigInfo = SigInfo(lambda x, **kwargs: None, 1, x=2)
        self.assertEqual(2, sigInfo["x"])

    def test_sigInfoCall(self):
        self.assertEqual(None, SigInfo(lambda: None).call())

        sigInfo = SigInfo(lambda x: x, 5)
        self.assertEqual(5, sigInfo.call())

        sigInfo["x"] = 3
        self.assertEqual(3, sigInfo.call())

        sigInfo["new"] = 4
        self.assertEqual(3, sigInfo.call())

        sigInfo["x"] = 3
        self.assertEqual(3, sigInfo.call())

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

    def test_calltable(self):
        call = CallTable("test")
        call.generate(print_out=False)
        call.generate_with_args(foo="bar", print_out=False)
        call.generate_with_funcs(length=len, print_out=False)

        call.set_args(foo="bars")
        self.assertIn("4", call.generate_with_funcs(length=len, print_out=False))

        call.set_funcs(type=type)
        self.assertIn("<class 'str'>", call.generate(print_out=False))

    def test_deco_define_comparisons(self):
        @Operators.deco_define_comparisons(lambda left: left.val)
        class Compare:
            def __init__(self, val):
                self.val = val

        a = Compare(1)
        b = Compare(2)
        self.assertEqual(True, a < b)
        self.assertEqual(False, a > b)
        self.assertEqual(False, a == b)
        self.assertEqual(True, a != b)
        self.assertEqual(True, a <= b)
        self.assertEqual(False, a >= b)

    def test_calculate(self):
        self.assertEqual(5, calculate("x + y", 2, 3))
        self.assertEqual(6, calculate("x * y", 2, 3))
        self.assertEqual(8, calculate("x + y * x", 2, 3))

    def test_deco_extend(self):
        @deco_extend
        class MyInt(int):
            def __init__(self, value, other):
                self.value = value
                self.other = other

        self.assertEqual(1, MyInt(1, 2))
        self.assertEqual(1, MyInt(1, 2).value)
        self.assertEqual(2, MyInt(1, 2).other)

    def test_deco_propagate_while(self):
        class A(int):
            @deco_propagate_while(False, lambda a: A(a + 1))
            def greater_than_10(self):
                return self > 10
        self.assertEqual(True, A(1).greater_than_10())

    def test_wrapper_transfer(self):
        def deco(func):
            def _wrapper():
                return func()
            return _wrapper

        def deco_transfer(func):
            def _wrapper():
                return func()
            return wrapper_transfer(func, _wrapper)

        @deco
        def x():
            """ Doc x. """

        @deco_transfer
        def y():
            """ Doc x. """

        self.assertEqual(None, x.__doc__)
        self.assertEqual("_wrapper", x.__name__)

        self.assertEqual(" Doc x. ", y.__doc__)
        self.assertEqual("y", y.__name__)

    def test_cache_clear(self):
        class A:
            bar = 2

            @classmethod
            @deco_cache()
            def foo(cls):
                return cls.bar

        self.assertEqual(2, A().foo())

        A.bar = 4
        self.assertEqual(2, A().foo())

        cache_clear(A)
        self.assertEqual(4, A().foo())

    def test_recycle(self):
        class A(Recycle):
            _recycle_keys = {}
            def __init__(self):
                pass
        a = A()
        self.assertIs(a, A())

        a.recycle_clear()
        self.assertIsNot(a, A())

        class B(Recycle):
            _recycle_keys = {"x": str}
            def __init__(self, x):
                self.y = []
        self.assertIs(B(x=1), B(1))
        self.assertIs(B(x=1).y, B(1).y)

        class C(TreeDiagram, Recycle):
            _recycle_keys = {"x": str}
            def __init__(self, x):
                pass
        self.assertIs(C(x=1), C(x=1))
        self.assertIs(C(x=1), C(x=1))

        self.assertIsNot(C(1), C(2))

        self.assertEqual(2, len(C._recycle_instances))
        C.recycle_clear_all()
        self.assertEqual(0, len(C._recycle_instances))

    def test_import_module(self):
        self.assertEqual("generallibrary", import_module("generallibrary").__name__)
        self.assertEqual("pandas", import_module("pandas").__name__)
        self.assertEqual(None, import_module("doesntexist", error=False))

    def test_terminal(self):
        self.assertEqual(0, terminal("-c", "assert 5 == 5", python=True))
        with self.assertRaises(Exception):
            self.assertEqual(0, terminal("-c", "assert 5 == 4", python=True, suppress=True))
























































