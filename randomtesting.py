from generalfile import Path

from generallibrary import *
import sys
from io import StringIO


# y = RedirectStdout(lambda x: Path("foo").write(x, overwrite=True))
#
#
# with y:
#     print("hi")
#     print("there")


import importlib_metadata

print(importlib_metadata.metadata('pandas').get_all('Provides-Extra'))



