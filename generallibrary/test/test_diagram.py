
from generallibrary.diagram import *
from generallibrary.objinfo.objinfo import hook

import unittest




class A(TreeDiagram):
    def __init__(self, foo, parent=None):
        self.foo = self.data_keys_add("foo", foo, use_in_repr=True)

    def __repr__(self):
        return str(self.foo)


class B(NetworkDiagram):
    def __init__(self, foo, parent=None):
        self.foo = foo

    def __repr__(self):
        return str(self.foo)


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
        self.assertEqual(a, d.get_parent(1))
        self.assertEqual(a, d.get_parent(-1))
        self.assertEqual(b, d.get_parent(-2))
        self.assertEqual([b, a], d.get_parents(depth=-1))

        b.remove()
        self.assertEqual(b, d.get_parent())
        self.assertEqual(None, d.get_parent().get_parent())
        self.assertEqual([b], d.get_parents(depth=-1))

        b = TreeDiagram(parent=a)
        self.assertEqual(a.get_children(), [c, b])

        c.set_index(1)
        self.assertEqual(a.get_children(), [b, c])

    def test_get_nodes(self):
        a = A(1)
        b = a.add(2)
        c = b.add(3)

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

        b.remove()
        self.assertEqual([a, d], a.get_all())

    def test_copy(self):
        a = TreeDiagram()
        b = TreeDiagram(parent=a)
        c = TreeDiagram(parent=a)
        d = TreeDiagram(parent=b)

        a_copy = a.copy_node().get_all()
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
        b = a.add(2)
        c = b.set_parent(3)
        d = c.add(4)
        e = d.set_parent(5)

        self.assertEqual([a, c], b.get_parents())
        self.assertEqual([c], a.get_spouses())
        self.assertEqual([a, c], a.get_spouses(include_self=True))
        self.assertEqual(c, a.get_spouse())

        self.assertEqual([c, e], a.get_spouses(depth=1))
        self.assertEqual([c, a], e.get_spouses(depth=1))
        self.assertEqual(a, e.get_spouse(index=1, depth=1))

        self.assertEqual([c], e.get_spouses(depth=0))

    def test_data_keys(self):
        a = A("bar")
        self.assertEqual("bar", a.foo)

        b = a.copy_node()
        self.assertEqual("bar", b.foo)

        b.foo = 5
        self.assertEqual(5, b.foo)

        self.assertEqual(5, b.copy_node().foo)

        b.set_parent(parent=a)
        self.assertEqual([b], a.get_children(filt=lambda node: node.foo == 5))

        c = A("hello", parent=b)
        self.assertEqual(c, b.get_child(filt=lambda node: node.foo == "hello"))

        self.assertEqual(["bar"], a.repr_list())

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
        markdown.add("foo", "bar")
        markdown.add(Markdown("hello", "there").wrap_with_tags("```"))
        markdown.add(Markdown("hi", "yo").wrap_with_tags("pre"))
        self.assertEqual(['foo', 'bar', '', '```', 'hello', 'there', '```', '', '<pre>', 'hi', 'yo', '</pre>'], markdown.get_all_lines())

        markdown1 = Markdown("line1", header="header1")
        markdown2 = markdown1.add(Markdown("line2", header="header2"))
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
        b = a.add(2)
        c = b.add(3)
        d = b.add(4)
        e = A(0)
        a.set_parent(e)

        self.assertEqual([e, a, b, c, d], a.get_ordered())
        self.assertEqual([[e], [a], [b], [c, d]], a.get_ordered(flat=False))

        self.assertEqual(0, e.get_ordered_index())
        self.assertEqual(1, a.get_ordered_index())
        self.assertEqual(2, b.get_ordered_index())
        self.assertEqual(3, c.get_ordered_index())
        self.assertEqual(3, d.get_ordered_index())






from generallibrary import initBases














