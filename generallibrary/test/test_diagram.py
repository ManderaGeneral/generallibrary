
import unittest

from generallibrary.versions import VerInfo
from generallibrary.diagram import TreeDiagram


class TreeDiagramTest(unittest.TestCase):
    def test_children(self):
        a = TreeDiagram()
        self.assertEqual([], a.get_children())
        self.assertEqual(None, a.get_child())

        b = TreeDiagram(parent=a)
        self.assertEqual([b], a.get_children())
        self.assertEqual(b, a.get_child())

        c = TreeDiagram(parent=a)
        self.assertEqual([b, c], a.get_children())
        self.assertEqual(b, a.get_child())
        self.assertEqual(None, b.get_child())

        d = TreeDiagram(parent=b)
        self.assertEqual([b, c], a.get_children())
        self.assertEqual(d, b.get_child())
        self.assertEqual(c, a.get_child(1))
        self.assertEqual(None, a.get_child(2))
        self.assertEqual(c, a.get_child(-1))

        b.remove()
        self.assertEqual([c], a.get_children())

        del a.get_children()[0]
        self.assertEqual([c], a.get_children())

    def test_parent(self):
        a = TreeDiagram()
        self.assertEqual(None, a.get_parent())
        self.assertEqual([], a.get_all_parents())

        b = TreeDiagram(parent=a)
        self.assertEqual(a, b.get_parent())
        self.assertEqual(None, b.get_parent(1))
        self.assertEqual([a], b.get_all_parents())

        c = TreeDiagram(parent=a)
        self.assertEqual(a, c.get_parent())
        self.assertEqual([a], c.get_all_parents())

        d = TreeDiagram(parent=b)
        self.assertEqual(b, d.get_parent())
        self.assertEqual(a, d.get_parent(1))
        self.assertEqual(a, d.get_parent(-1))
        self.assertEqual(b, d.get_parent(-2))
        self.assertEqual([b, a], d.get_all_parents())

        b.remove()
        self.assertEqual(b, d.get_parent())
        self.assertEqual(None, d.get_parent().get_parent())
        self.assertEqual([b], d.get_all_parents())

        b = TreeDiagram(parent=a)
        self.assertEqual(a.get_children(), [c, b])

        c.set_index(1)
        self.assertEqual(a.get_children(), [b, c])

    def test_get_all(self):
        a = TreeDiagram()
        self.assertEqual([a], a.get_all())

        b = TreeDiagram(parent=a)
        self.assertEqual([a, b], a.get_all())

        c = TreeDiagram(parent=a)
        self.assertEqual([a, b, c], a.get_all())

        d = TreeDiagram(parent=b)
        self.assertEqual([a, b, d, c], a.get_all())

        b.remove()
        self.assertEqual([a, c], a.get_all())

    def test_copy_to(self):
        a = TreeDiagram()
        b = TreeDiagram(parent=a)
        c = TreeDiagram(parent=a)
        d = TreeDiagram(parent=b)

        a_copy = a.copy_to().get_all()
        self.assertEqual(str(a.get_all()), str(a_copy))

        b.remove()
        self.assertNotEqual(str(a.get_all()), str(a_copy))

    def test_siblings(self):
        a = TreeDiagram()
        self.assertEqual([], a.get_siblings())

        b = TreeDiagram(parent=a)
        self.assertEqual([], a.get_siblings())
        self.assertEqual([], b.get_siblings())

        c = TreeDiagram(parent=a)
        self.assertEqual([], a.get_siblings())
        self.assertEqual([c], b.get_siblings())
        self.assertEqual([b], c.get_siblings())

        d = TreeDiagram(parent=b)
        self.assertEqual([], a.get_siblings())
        self.assertEqual([c], b.get_siblings())
        self.assertEqual([b], c.get_siblings())
        self.assertEqual([], d.get_siblings())

        e = TreeDiagram(parent=a)
        self.assertEqual([c, e], b.get_siblings())


        self.assertEqual(None, a.get_next_sibling())
        self.assertEqual(None, a.get_previous_sibling())

        self.assertEqual(c, b.get_next_sibling())
        self.assertEqual(None, b.get_previous_sibling())

        self.assertEqual(e, c.get_next_sibling())
        self.assertEqual(b, c.get_previous_sibling())

        self.assertEqual(None, e.get_next_sibling())
        self.assertEqual(c, e.get_previous_sibling())

    def test_data_keys(self):
        from generallibrary import initBases
        @initBases
        class A(TreeDiagram):
            def __init__(self, foo):
                self.foo = self.data_keys_add("foo", foo)

        a = A("bar")
        self.assertEqual("bar", a.foo)

        b = a.copy_to()
        self.assertEqual("bar", b.foo)

        b.foo = 5
        self.assertEqual(5, b.foo)

        self.assertEqual(5, b.copy_to().foo)

















