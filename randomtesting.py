from generallibrary import *

from generalfile import Path


# Path("hi.md").text.write(Markdown("hi", header="hello", collapsible=True), overwrite=True)

a = Markdown("a")
a.add_node("b").add_node("c")
a.add_node("d")

print(a)

