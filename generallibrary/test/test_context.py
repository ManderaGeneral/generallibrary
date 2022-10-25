from unittest import TestCase

from generallibrary.context import *


class TestContext(TestCase):
    def test_decocontext_simple_deco_no_call(self):
        glob = []
        class X(DecoContext):
            def before(self):
                glob.append(1)
            def after(self):
                glob.append(3)
        @X
        def x():
            glob.append(2)
        x()
        self.assertEqual([1, 2, 3], glob)

    def test_decocontext_simple_deco_with_call(self):
        glob = []
        class X(DecoContext):
            def before(self):
                glob.append(1)
            def after(self):
                glob.append(3)
        @X()
        def x():
            glob.append(2)
        x()
        self.assertEqual([1, 2, 3], glob)

    def test_decocontext_simple_deco_on_method(self):
        glob = []
        class X(DecoContext):
            def before(self):
                glob.append(1)
            def after(self):
                glob.append(3)

        class Y:
            @X
            def x(self):
                glob.append(2)
        Y().x()
        self.assertEqual([1, 2, 3], glob)

    def test_decocontext_simple_deco_on_method_called(self):
        glob = []
        class X(DecoContext):
            def before(self):
                glob.append(1)
            def after(self):
                glob.append(3)

        class Y:
            @X()
            def x(self):
                glob.append(2)
        Y().x()
        self.assertEqual([1, 2, 3], glob)

    def test_decocontext_simple_context(self):
        glob = []
        class X(DecoContext):
            def before(self):
                glob.append(1)
            def after(self):
                glob.append(3)
        with X():
            glob.append(2)
        self.assertEqual([1, 2, 3], glob)

    def test_decocontext_one_par_deco_no_call(self):
        glob = []
        class X(DecoContext):
            def __init__(self, func, foo):  # func required
                self.foo = foo
            def before(self):
                glob.append(self.foo)
                glob.append(1)
            def after(self):
                glob.append(3)
                glob.append(self.foo)
        @X
        def x():
            glob.append(2)
        x()
        self.assertEqual([None, 1, 2, 3, None], glob)

    def test_decocontext_one_par_deco_with_call_positional(self):
        glob = []
        class X(DecoContext):
            def __init__(self, foo):
                self.foo = foo
            def before(self):
                glob.append(self.foo)
                glob.append(1)
            def after(self):
                glob.append(3)
                glob.append(self.foo)
        @X("bar")
        def x():
            glob.append(2)
        x()
        self.assertEqual(["bar", 1, 2, 3, "bar"], glob)

    def test_decocontext_one_par_deco_with_call_kw(self):
        glob = []
        class X(DecoContext):
            def __init__(self, foo):
                self.foo = foo
            def before(self):
                glob.append(self.foo)
                glob.append(1)
            def after(self):
                glob.append(3)
                glob.append(self.foo)
        @X(foo="bar")
        def x():
            glob.append(2)
        x()
        self.assertEqual(["bar", 1, 2, 3, "bar"], glob)

    def test_decocontext_one_par_context_positional(self):
        glob = []
        class X(DecoContext):
            def __init__(self, foo):
                self.foo = foo
            def before(self):
                glob.append(self.foo)
                glob.append(1)
            def after(self):
                glob.append(3)
                glob.append(self.foo)
        with X("bar"):
            glob.append(2)
        self.assertEqual(["bar", 1, 2, 3, "bar"], glob)

    def test_decocontext_one_par_context_kw(self):
        glob = []
        class X(DecoContext):
            def __init__(self, foo):
                self.foo = foo
            def before(self):
                glob.append(self.foo)
                glob.append(1)
            def after(self):
                glob.append(3)
                glob.append(self.foo)
        with X(foo="bar"):
            glob.append(2)
        self.assertEqual(["bar", 1, 2, 3, "bar"], glob)

    def test_decocontext_exception_deco(self):
        glob = []
        class X(DecoContext):
            def before(self):
                glob.append(1)
            def after(self):
                glob.append(3)
        @X
        def x():
            glob.append(2)
            raise Exception

        self.assertRaises(Exception, x)
        self.assertEqual([1, 2, 3], glob)

    def test_decocontext_exception_context(self):
        glob = []
        class X(DecoContext):
            def before(self):
                glob.append(1)
            def after(self):
                glob.append(3)

        def x():
            with X():
                glob.append(2)
                raise Exception

        self.assertRaises(Exception, x)
        self.assertEqual([1, 2, 3], glob)

class TestRedirectStdout(TestCase):
    def test_redirect_simple_context_list(self):
        x = []
        with RedirectStdout(x):
            print("foo")
        self.assertEqual(["foo"], x)

    def test_redirect_simple_deco_list(self):
        x = []
        @RedirectStdout(x)
        def y():
            print("foo")
        y()
        self.assertEqual(["foo"], x)

    def test_redirect_simple_context_none(self):
        with RedirectStdout():
            print("ERROR - This shouldn't print (Hard to find though...)")

    def test_redirect_simple_deco_none(self):
        @RedirectStdout
        def y():
            print("ERROR - This shouldn't print (Hard to find though...)")

    def test_redirect_method(self):
        class X:
            @RedirectStdout()
            def y(self):
                print("ERROR - This shouldn't print (Hard to find though...)")

        X().y()

    def test_redirect_method_without_call_and_func_arg(self):
        class X:
            @RedirectStdout
            def y(self):
                print("ERROR - This shouldn't print (Hard to find though...)")

        self.assertRaises(AssertionError, X().y)

