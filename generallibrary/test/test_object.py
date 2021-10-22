
from generallibrary.object import *
from generallibrary.objinfo.objinfo import ObjInfo, hook
from generallibrary.functions import initBases, AutoInitBases

import unittest


# hook couldn't get foo's parent if defined inside method
class hook_A:
    def foo(self):
        return 1
class hook_B(hook_A):
    pass
hook_glob = 0

hook_bar = []
def hook_foo():
    hook_bar.append(1)


class ObjectTest(unittest.TestCase):  # This line is used for test_get_definition_line
    def test_AutoInitBases(self):
        class A(metaclass=AutoInitBases):
            def __init__(self):
                self.x = 1

        class B(A):
            def __init__(self):
                self.y = 2

        self.assertEqual(1, B().x)
        self.assertEqual(2, B().y)

    def test_hook_method_base(self):
        global hook_glob
        hook_glob = 0

        def change_glob():
            global hook_glob
            hook_glob += 1

        hook(hook_B.foo, change_glob, owner=hook_B)

        self.assertEqual(0, hook_glob)
        hook_A().foo()
        self.assertEqual(0, hook_glob)
        hook_B().foo()
        self.assertEqual(1, hook_glob)

    def test_hook_func(self):
        hook(hook_foo, lambda: hook_bar.append(0), after=False)
        hook(hook_foo, lambda: hook_bar.append(2), after=True)
        hook_foo()
        self.assertEqual([0, 1, 2], hook_bar)


    def test_getsize(self):
        """ Hard to make too specific tests I think due to 64-bit vs 32-bit for example. """
        x = []
        y = "hi"
        z = [y]
        self.assertGreater(getsize(z), getsize(x) + getsize(y))  # See that there's overhead

    def test_initBases(self):
        # One argument without default
        class Base:
            def __init__(self, x):
                self.x = x

        @initBases
        class Parent(Base):
            def __init__(self, x):
                self.y = 2

        self.assertEqual(5, Parent(x=5).x)
        self.assertEqual(5, Parent(5).x)
        self.assertEqual(2, Parent(x=5).y)
        self.assertEqual(2, Parent(5).y)

        # One argument without default and one value with default inside Base
        class Base:
            def __init__(self, x, z=6):
                self.x = x
                self.z = z

        @initBases
        class Parent(Base):
            def __init__(self, x, z=None):
                self.y = 2
        self.assertEqual(5, Parent(x=5).x)
        self.assertEqual(2, Parent(x=5).y)
        self.assertIs(None, Parent(x=5).z)
        self.assertEqual(4, Parent(x=5, z=4).z)

        # One argument without default and one value with default inside Parent
        class Base:
            def __init__(self, x, z):
                self.x = x
                self.z = z

        @initBases
        class Parent(Base):
            def __init__(self, x, z=None):
                self.y = 2

        self.assertEqual(5, Parent(x=5).x)
        self.assertEqual(2, Parent(x=5).y)
        self.assertEqual(None, Parent(x=5).z)
        self.assertEqual(4, Parent(x=5, z=4).z)

        # Base without init
        class Base:
            def test(self):
                pass

        @initBases
        class Parent(Base):
            def __init__(self, x):
                self.x = x
                self.y = 2

        self.assertEqual(5, Parent(x=5).x)
        self.assertEqual(2, Parent(x=5).y)

        # Two bases, seperate args
        class Base:
            def __init__(self, x):
                self.x = x

        class Base2:
            def __init__(self, y):
                self.y = y

        @initBases
        class Parent(Base, Base2):
            def __init__(self, x, y):
                pass

        self.assertEqual(5, Parent(x=5, y=2).x)
        self.assertEqual(2, Parent(x=5, y=2).y)

        # Two bases, same args
        class Base:
            def __init__(self, x):
                self.x = x
        class Base2:
            def __init__(self, x):
                self.y = x

        @initBases
        class Parent(Base, Base2):
            def __init__(self, x):
                pass

        self.assertEqual(5, Parent(x=5).x)
        self.assertEqual(5, Parent(x=5).y)

        # One base taking *args
        class Base:
            def __init__(self, *x):
                self.x = x

        @initBases
        class Parent(Base):
            def __init__(self, *x):
                pass
        self.assertEqual((5, ), Parent(5).x)

    def test_hierarchy(self):
        class C:
            def __init__(self, c, d=4):
                self.c = c
                self.d = d

        @initBases
        class B(C):
            def __init__(self, b, c):
                self.b = b

        @initBases
        class A(B):
            def __init__(self, b, c):
                pass

        a = A(b=2, c=3)

        self.assertEqual(2, a.b)
        self.assertEqual(3, a.c)
        self.assertEqual(4, a.d)

        self.assertEqual(1, A(1, 2).b)
        self.assertEqual(1, A(1, c=2).b)

    def test_hierarchy_empty_middleman(self):
        class C:
            def __init__(self, a, b=2):
                self.a = a
                self.b = b

        @initBases
        class B(C):
            pass

        @initBases
        class A(B):
            def __init__(self, a, b=None):
                pass

        self.assertEqual(5, A(5).a)
        self.assertEqual(5, A(a=5).a)

        self.assertEqual(None, A(5).b)

    def test__init_post__(self):
        glob = []

        class A:
            def __init__(self):
                glob.append(1)

            def __init_post__(self):
                glob.append(4)

        @initBases
        class B(A):
            def __init__(self):
                glob.append(2)

            def __init_post__(self):
                glob.append(5)

        @initBases
        class C(B):
            def __init__(self):
                glob.append(3)

            def __init_post__(self):
                glob.append(6)

        @initBases
        class D(C):
            def __init_post__(self):
                glob.append(7)

        D()
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], glob)

    def test_ObjInfo(self):
        def check(bound_method):
            """ Check that the correct method is True and all other are False. """
            objInfo = getattr(bound_method, "__self__")
            for name, method in objInfo.type_methods.items():
                method_is_bound_method = bound_method == getattr(objInfo, name)
                result = method(self=objInfo)
                if result is not method_is_bound_method:
                    raise AssertionError(f"{objInfo.obj} returns {result} for {name}.")

        check(ObjInfo(unittest).is_module)
        check(ObjInfo(a).is_function)
        check(ObjInfo(a()).is_function)
        check(ObjInfo(_Foo).is_class)
        check(ObjInfo(_Foo()).is_instance)

        check(ObjInfo(_Foo._self).is_method)
        check(ObjInfo(_Foo()._self).is_method)

        check(ObjInfo(_Foo._cls).is_method)
        check(ObjInfo(_Foo()._cls).is_method)

        check(ObjInfo(_Foo._static).is_method)
        check(ObjInfo(_Foo()._static).is_method)

        check(ObjInfo(_Foo._property).is_property)

    def test_ObjInfo_parents(self):
        objInfo = ObjInfo(ObjInfo)
        self.assertEqual("generallibrary", objInfo.get_parent(depth=-1, index=-1).obj.__name__)

    def test_ObjInfo_protected(self):
        objInfo = ObjInfo(_Foo)
        objInfo.children_states = {}

        self.assertEqual(True, objInfo.get_child(filt=lambda node: node.name == "_self", traverse_excluded=True).protected())
        self.assertEqual(False, objInfo.get_child(filt=lambda node: node.name == "self", traverse_excluded=True).protected())

        self.assertEqual(True, objInfo.get_child(filt=lambda node: node.name == "_attr", traverse_excluded=True).protected())
        self.assertEqual(False, objInfo.get_child(filt=lambda node: node.name == "attr", traverse_excluded=True).protected())

        self.assertEqual(False, objInfo.get_child(filt=lambda node: node.name == "_Foo__private", traverse_excluded=True).protected())
        self.assertEqual(True, objInfo.get_child(filt=lambda node: node.name == "_Foo__private", traverse_excluded=True).private())
        self.assertEqual(True, objInfo.get_child(filt=lambda node: node.name == "_Foo__private", traverse_excluded=True).internal())
        self.assertEqual(False, objInfo.get_child(filt=lambda node: node.name == "_Foo__private", traverse_excluded=True).public())

        self.assertEqual(False, ObjInfo(a).protected())
        self.assertEqual(False, ObjInfo(a()).protected())

    def test_check_if_parent_eligible(self):
        self.assertEqual(True, ObjInfo.check_if_parent_eligible(sys.modules["test_object"], _Foo, "_Foo"))
        self.assertEqual(False, ObjInfo.check_if_parent_eligible(sys.modules["test_object"], _Foo, "Foo"))
        self.assertEqual(False, ObjInfo.check_if_parent_eligible(sys.modules["test_object"], _Foo.self, "self"))
        self.assertEqual(True, ObjInfo.check_if_parent_eligible(_Foo, _Foo.self, "self"))

    def test_doc(self):
        def foo():
            """ bar
                hello """
        self.assertEqual("bar\nhello", ObjInfo(foo).doc(only_first_line=False))
        self.assertEqual("bar", ObjInfo(foo).doc(only_first_line=True))
        self.assertRaises(AttributeError, ObjInfo(foo).doc, require_sentence=True)

        def empty():
            pass

        self.assertEqual("", ObjInfo(empty).doc(only_first_line=False))
        self.assertEqual("", ObjInfo(empty).doc(only_first_line=True))
        self.assertRaises(AttributeError, ObjInfo(empty).doc, require_sentence=True)

        def proper():
            """ Proper. """

        self.assertEqual("Proper.", ObjInfo(proper).doc(only_first_line=False))
        self.assertEqual("Proper.", ObjInfo(proper).doc(only_first_line=True))
        self.assertEqual("Proper.", ObjInfo(proper).doc(require_sentence=True))

    def test_defined_by_parent(self):
        self.assertEqual(True, ObjInfo(_Foo.self).defined_by_parent())
        self.assertEqual(True, ObjInfo(_Bar.self).defined_by_parent())
        self.assertEqual(True, ObjInfo(_Foo._self).defined_by_parent())
        self.assertEqual(False, ObjInfo(_Bar._self, parent=ObjInfo(_Bar)).defined_by_parent())  # Gotta set parent manually, otherwise it'll be _Foo

    def test_file(self):
        self.assertEqual("test_object.py", ObjInfo(_Foo).file(relative=True))
        self.assertEqual("test_object.py", ObjInfo(_Foo.self).file(relative=True))

    def test_origins(self):
        self.assertEqual(True, ObjInfo(_Foo.self).from_class())
        self.assertEqual(False, ObjInfo(_Bar.self).from_class())

        self.assertEqual(False, ObjInfo(_Bar.uhm).from_base())

        self.assertEqual(False, ObjInfo(_Bar.uhm).from_builtin())
        self.assertEqual(True, ObjInfo("".startswith).from_builtin())

        self.assertEqual(False, ObjInfo(_Bar.attr).from_instance())

        self.assertEqual(True, ObjInfo(_Bar).from_module())
        self.assertEqual(False, ObjInfo(_Bar.self).from_module())

        objInfo = ObjInfo(_Bar())
        self.assertEqual(True, objInfo.get_child(filt=lambda node: node.name == "instance_var", traverse_excluded=True).from_instance())
        self.assertEqual(True, objInfo.get_child(filt=lambda node: node.name == "self", traverse_excluded=True).from_base())

    def test_get_definition_line(self):
        self.assertEqual(22, ObjInfo(ObjectTest).get_definition_line())

    def test_get_origin(self):
        class FooBar:
            @property
            def test(self):
                return

        self.assertEqual("test", ObjInfo(FooBar.test).name)
        self.assertEqual("test", ObjInfo.get_origin(FooBar.test).__name__)

    def test_identifier(self):
        self.assertEqual(ObjInfo(_Foo).identifier(), ObjInfo(_Foo).identifier())

    def test_repr(self):
        objInfo = ObjInfo(_Foo)
        self.assertEqual(True, "_Foo" in repr(objInfo))
        self.assertEqual(True, "Class" in repr(objInfo))


class _Foo:
    _attr = 5
    attr = 3

    def self(self):
        """ Not protected. """
        pass

    def _self(self):
        pass

    @classmethod
    def _cls(cls):
        pass

    @staticmethod
    def _static():
        pass

    @property
    def _property(self):
        return

    def __private(self):
        pass


class _Bar(_Foo):
    def __init__(self):
        self.instance_var = 4

    def uhm(self):
        pass

    def self(self):
        """ Not protected. """
        pass


def a():
    def b():
        pass
    return b

















