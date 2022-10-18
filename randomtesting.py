from generallibrary import *

from generalfile import Path


# Path("hi.md").text.write(Markdown("hi", header="hello", collapsible=True), overwrite=True)

a = Markdown("hi", collapsible=True).wrap_with_tags("```")

a.add_node("hello", collapsible=True).wrap_with_tags("<>")

a.get_all_lines()

