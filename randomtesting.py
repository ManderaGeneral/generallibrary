from generalfile import Path

from generallibrary import *



class X(TreeDiagram):
    def __str__(self):
        return "hi"

a = X()

b = a.add_node()
c = b.add_node()
c.add_node(a)

Path("hi.md").text.write(a.mermaid(), overwrite=True)



