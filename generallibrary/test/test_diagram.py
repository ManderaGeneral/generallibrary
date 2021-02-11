
from generallibrary.diagram import *

import unittest


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
        tester = self
        @initBases
        class A(TreeDiagram):
            def __init__(self, foo):
                self.foo = self.data_keys_add("foo", foo, use_in_repr=True)
            def hook_set_attribute(self, key, value, old_value):
                if old_value is not None:
                    tester.assertEqual(("foo", 5, "bar"), (key, value, old_value))

        a = A("bar")
        self.assertEqual("bar", a.foo)

        b = a.copy_to()
        self.assertEqual("bar", b.foo)

        b.foo = 5
        self.assertEqual(5, b.foo)

        self.assertEqual(5, b.copy_to().foo)

        b.set_parent(parent=a)
        self.assertEqual([b], a.get_children_by_key_values(foo=5))

        c = A("hello").set_parent(parent=b)
        self.assertEqual(c, b.get_child_by_key_values(foo="hello"))

        self.assertEqual(["bar"], a.repr_list())

    def test_hooks(self):
        x = []
        @initBases
        class A(TreeDiagram):
            def hook_create_pre(self): x.append(0)
            def __init__(self, parent=None): x.append(1)
            def hook_new_parent(self, parent, old_parent): x.append(2)
            def hook_create_post(self): x.append(3)
            def hook_lose_parent(self, old_parent, parent): x.append(4)
            def hook_new_child(self, child): x.append(5)
            def hook_lose_child(self, child): x.append(6)
            def hook_remove(self): x.append(7)


        a = A(parent=TreeDiagram())

        parent = TreeDiagram()
        a.set_parent(parent=parent)
        TreeDiagram(parent=a).remove()
        a.remove()

        self.assertEqual([0, 1, 2, 3, 4, 2, 5, 6, 4, 7], x)

    def test_save_with_keys(self):
        @initBases
        class A(TreeDiagram):
            def __init__(self, foo, parent=None):
                self.foo = self.data_keys_add("foo", foo)

        a = A("hi")
        b = A("there", parent=a)

        self.assertEqual(a.save(), A.load(a.save()).save())
        self.assertEqual("there", A.load(a.save()).get_child().foo)

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
        a = NetworkDiagram()
        self.assertEqual(set(), a.get_nodes())
        self.assertEqual(set(), a.get_links())

        b = NetworkDiagram()
        a.link(b)
        self.assertEqual({b}, a.get_nodes())
        self.assertEqual(set(), a.get_nodes(outgoing=False))
        self.assertEqual({b}, a.get_nodes(incoming=False))

        self.assertEqual({a.get_link(b)}, a.get_links())
        self.assertEqual({a, b}, a.get_nodes_all())
        self.assertEqual({a, b}, a.get_routes().get_nodes())

        self.assertEqual([{a}, {b}], a.get_ordered())
        self.assertEqual(0, a.get_ordered_index())
        self.assertEqual(1, b.get_ordered_index())
        self.assertEqual([a, b], b.get_ordered_flat())





from generallibrary import initBases














