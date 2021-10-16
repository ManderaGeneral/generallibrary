
from generallibrary.diagram import *

import unittest


class A(TreeDiagram):
    def __init__(self, foo, parent=None):
        self.foo = foo

    def __repr__(self):
        return str(self.foo)


class B(NetworkDiagram):
    def __init__(self, foo, parent=None):
        self.foo = foo

    def __repr__(self):
        return str(self.foo)


class TreeDiagramTest(unittest.TestCase):
    def test_singular(self):
        a = A(1)
        b = a.add_node(2)
        c = b.add_node(3)

        self.assertEqual(b, c.get_parent(depth=1))
        self.assertEqual(a, c.get_parent(depth=1, index=1))

    def test_children(self):
        a = TreeDiagram()
        self.assertEqual([], a.get_children())
        self.assertEqual(None, a.get_child())

        b = TreeDiagram(parent=a)
        self.assertEqual([b], a.get_children())
        self.assertEqual(b, a.get_child())

        self.assertEqual(a, b.get_parent())
        self.assertEqual(b, b.get_parent(include_self=True))
        self.assertEqual(a, b.get_parent(include_self=True, filt=lambda x: x is not b, traverse_excluded=True))
        self.assertEqual(None, b.get_parent(filt=lambda path: False))

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

        b.set_parent(None)
        self.assertEqual([c], a.get_children())

        del a.get_children()[0]
        self.assertEqual([c], a.get_children())

        e = TreeDiagram(parent=a)
        f = TreeDiagram(parent=a)

        self.assertEqual(0, d.get_index())
        self.assertEqual(1, e.get_index())
        self.assertEqual(2, f.get_index())
        self.assertEqual(0, a.get_index())


    def test_parent(self):
        a = TreeDiagram()
        self.assertEqual(None, a.get_parent())
        self.assertEqual([], a.get_parents(depth=-1))

        b = TreeDiagram(parent=a)
        self.assertEqual(a, b.get_parent())
        self.assertEqual(None, b.get_parent(1))
        self.assertEqual([a], b.get_parents(depth=-1))

        c = TreeDiagram(parent=a)
        self.assertEqual(a, c.get_parent())
        self.assertEqual([a], c.get_parents(depth=-1))

        d = TreeDiagram(parent=b)
        self.assertEqual(b, d.get_parent())
        self.assertEqual(a, d.get_parent(1, 1))
        self.assertEqual(a, d.get_parent(-1, -1))
        self.assertEqual(b, d.get_parent(-2, -2))
        self.assertEqual([b, a], d.get_parents(depth=-1))

        b.set_parent(None)
        self.assertEqual(b, d.get_parent())
        self.assertEqual(None, d.get_parent().get_parent())
        self.assertEqual([b], d.get_parents(depth=-1))

        b = TreeDiagram(parent=a)
        self.assertEqual(a.get_children(), [c, b])

        c.set_index(1)
        self.assertEqual(a.get_children(), [b, c])

    def test_get_nodes(self):
        a = A(1)
        b = a.add_node(2)
        c = b.add_node(3)

        self.assertEqual([a, c], b.get_nodes())
        self.assertEqual([b], a.get_nodes())
        self.assertEqual([b, c], a.get_nodes(1))
        self.assertEqual([b, c], a.get_nodes(-1))
        self.assertEqual([a, b], a.get_nodes(include_self=True))

        self.assertEqual(b, a.get_node())
        self.assertEqual(None, a.get_node(1))
        self.assertEqual(c, a.get_node(1, 1))
        self.assertEqual(a, b.get_node())
        self.assertEqual(c, b.get_node(1))

    def test_get_all(self):
        a = A(1)
        self.assertEqual([a], a.get_all())

        b = A(2, parent=a)
        self.assertEqual([a, b], a.get_all())

        c = A(3, parent=b)
        self.assertEqual([a, b, c], a.get_all())

        d = A(4, parent=a)
        self.assertEqual([a, b, c, d], a.get_all())

        b.set_parent(None)
        self.assertEqual([a, d], a.get_all())

    def test_copy_node(self):
        a = TreeDiagram()
        b = TreeDiagram(parent=a)
        c = TreeDiagram(parent=a)
        d = TreeDiagram(parent=b)

        a_copy = a.copy_node().get_all()
        self.assertEqual(len(a.get_all()), len(a_copy))

        x = B(3)
        self.assertEqual(x.foo, x.copy_node().foo)

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


        self.assertEqual(None, a.get_sibling())
        self.assertEqual(None, a.get_sibling(-1))

        self.assertEqual(c, b.get_sibling())
        self.assertEqual(e, b.get_sibling(-1))

        self.assertEqual(e, c.get_sibling())
        self.assertEqual(b, c.get_sibling(-1))

        self.assertEqual(b, e.get_sibling())
        self.assertEqual(c, e.get_sibling(-1))

    def test_get_spouses(self):
        a = B(1)
        b = a.add_node(2)
        c = b.set_parent(3)
        d = c.add_node(4)
        e = d.set_parent(5)

        self.assertEqual([a, c], b.get_parents())
        self.assertEqual([c], a.get_spouses())
        self.assertEqual([a, c], a.get_spouses(include_self=True))
        self.assertEqual(c, a.get_spouse())

        self.assertEqual([c, e], a.get_spouses(depth=1))
        self.assertEqual([c, a], e.get_spouses(depth=1))
        self.assertEqual(a, e.get_spouse(index=1, depth=1))

        self.assertEqual([c], e.get_spouses(depth=0))

    def test_save_with_keys(self):
        a = A("hi")
        b = A("there", parent=a)

        self.assertEqual(a.save_node(), A.load_node(a.save_node()).save_node())
        self.assertEqual("there", A.load_node(a.save_node()).get_child().foo)

    def test_view(self):
        a = TreeDiagram()
        b = TreeDiagram(parent=a)
        c = TreeDiagram(parent=a)
        d = TreeDiagram(parent=b)

        self.assertEqual(4, len(a.view(print_out=False).splitlines()))
        self.assertEqual(2, len(b.view(print_out=False).splitlines()))
        self.assertEqual(1, len(c.view(print_out=False).splitlines()))
        self.assertEqual(1, len(d.view(print_out=False).splitlines()))

        self.assertEqual(4, len(a.view(relative=True, print_out=False).splitlines()))

    def test_markdown(self):
        self.assertEqual("foo\nbar", str(Markdown().add_lines("foo", "bar")))
        self.assertEqual("```\nfoo\n```", str(Markdown().add_code_lines("foo")))
        self.assertEqual(" - foo\n - bar", str(Markdown().add_list_lines("foo", "bar")))
        self.assertEqual(" - foo\n   - bar", str(Markdown().add_list_lines("foo").add_list_lines("bar", indent=1)))
        self.assertEqual("<pre>\nfoo\nbar\n</pre>", str(Markdown().add_pre_lines("foo", "bar")))
        self.assertEqual("| foo   |\n|:------|\n| bar   |", str(Markdown().add_table_lines({"foo": "bar"})))

        markdown = Markdown()
        markdown.add_node("foo", "bar")
        markdown.add_node(Markdown("hello", "there").wrap_with_tags("```"))
        markdown.add_node(Markdown("hi", "yo").wrap_with_tags("pre"))
        self.assertEqual(['foo', 'bar', '', '```', 'hello', 'there', '```', '', '<pre>', 'hi', 'yo', '</pre>'], markdown.get_all_lines())

        markdown1 = Markdown("line1", header="header1")
        markdown2 = markdown1.add_node(Markdown("line2", header="header2"))
        self.assertEqual(['# header1', 'line1'], markdown1.get_section_lines())
        self.assertEqual(['## header2', 'line2'], markdown1.get_child().get_section_lines())
        self.assertEqual(['# header1', 'line1', '', '## header2', 'line2'], markdown1.get_all_lines())

    def test_network_diagram(self):
        a1 = A(1)
        a2 = A(2)
        a3 = A(3)
        a1.set_parent(a2)
        a1.set_parent(a3)
        self.assertEqual([a3], a1.get_parents())

        a1 = B(1)
        a2 = B(2)
        a3 = B(3)
        a1.set_parent(a2)
        a1.set_parent(a3)
        self.assertEqual([a2, a3], a1.get_parents())

    def test_get_ordered(self):
        a = A(1)
        b = a.add_node(2)
        c = b.add_node(3)
        d = b.add_node(4)
        e = A(0)
        a.set_parent(e)

        self.assertEqual([e, a, b, c, d], a.get_ordered())
        self.assertEqual([[e], [a], [b], [c, d]], a.get_ordered(flat=False))

        self.assertEqual(0, e.get_ordered_index())
        self.assertEqual(1, a.get_ordered_index())
        self.assertEqual(2, b.get_ordered_index())
        self.assertEqual(3, c.get_ordered_index())
        self.assertEqual(3, d.get_ordered_index())

    def test_spawn(self):
        class Spawn(TreeDiagram):
            def __init__(self, x, parent=None):
                self.x = x

            def __str__(self):
                return str(self.x)

            def __repr__(self):
                return str(self)

            def spawn_parents(self):
                if not self._parents and self.x < 5:
                    self.set_parent(self.x + 1)

            def spawn_children(self):
                if not self._children and self.x > 0:
                    Spawn(self.x - 1, parent=self)

        # spawn = Spawn(2)
        # self.assertEqual([], spawn.get_children(spawn=False))
        # self.assertEqual([], spawn.get_children(filt=lambda node: False))
        # self.assertEqual([], spawn.get_children(spawn=False))

        self.assertEqual(None, Spawn(2).get_parent(spawn=False))
        self.assertEqual(3, Spawn(2).get_parent().x)

        self.assertEqual(None, Spawn(2).get_child(spawn=False))
        self.assertEqual(1, Spawn(2).get_child().x)

        self.assertEqual(None, Spawn(2).get_sibling(spawn=False))
        self.assertEqual(None, Spawn(2).get_sibling())

        spawn = Spawn(2)
        self.assertEqual([], [x.x for x in spawn.get_parents(spawn=False)])
        self.assertEqual([3], [x.x for x in spawn.get_parents()])
        self.assertEqual([3], [x.x for x in spawn.get_parents()])

        self.assertEqual([], [x.x for x in spawn.get_children(spawn=False)])
        self.assertEqual([1], [x.x for x in spawn.get_children()])
        self.assertEqual([1], [x.x for x in spawn.get_children()])

        self.assertEqual([], [x.x for x in Spawn(2).get_nodes(spawn=False)])
        self.assertEqual([3, 1], [x.x for x in Spawn(2).get_nodes()])

        self.assertEqual([5, 4, 3, 2, 1, 0], [x.x for x in Spawn(2).get_ordered()])

    def test_remove_node(self):
        a = A(1)
        b = a.add_node(2)
        c = b.add_node(3)

        self.assertEqual([b], a.get_children())
        self.assertEqual([c], b.get_children())

        a.remove_node()
        self.assertEqual([], a.get_children())
        self.assertEqual([], b.get_children())

    def test_remove_node_recycle(self):
        from generallibrary.functions import Recycle

        class C(TreeDiagram, Recycle):
            _recycle_keys = {"x": str}

            def __init__(self, x, parent=None):
                self.x = x

        a = C(1)
        self.assertIs(a, C(1))

        b = a.add_node(2)
        self.assertIs(b, C(2))

        b.remove_node()
        self.assertIsNot(b, C(2))

        b = a.add_node(2)
        self.assertIs(a, b.get_parent())

        c = b.add_node(3)
        self.assertIs(c, C(3))
        a.remove_node()
        self.assertIsNot(c, C(3))

    def test_filt(self):
        a = A(1)
        b = a.add_node(2)
        c = b.add_node(3)

        self.assertEqual(a, c.get_parent(depth=-1, filt=lambda node: node == a, traverse_excluded=True))

    def test_traverse_excluded(self):
        a = A(1)
        b = a.add_node(2)
        c = b.add_node(3)

        self.assertEqual([b, c], a.get_children(depth=-1))
        self.assertEqual([c], a.get_children(depth=-1, filt=lambda node: node != b, traverse_excluded=True))
        self.assertEqual([], a.get_children(depth=-1, filt=lambda node: node != b, traverse_excluded=False))

    def test_disconnect(self):
        a = A(1)
        b = a.add_node(2)
        c = b.add_node(3)

        c.disconnect(lambda node: node is b)

        self.assertEqual([a], a.get_all())








from generallibrary import initBases














