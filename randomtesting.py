from generallibrary import *

from generalfile import Path


Path("hi.md").text.write(Markdown("hi", header="hello", collapsible=True), overwrite=True)
