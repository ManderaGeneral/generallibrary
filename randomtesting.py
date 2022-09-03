from generalfile import Path

from generallibrary import *
import sys
from io import StringIO


y = RedirectStdout(lambda x: Path("foo").write(x, overwrite=True))


with y:
    print("hi")
    print("there")


