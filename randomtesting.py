
from generallibrary.time import Timer
from generallibrary.types import typeChecker, depth, getBaseClasses, getBaseClassNames
from generallibrary.iterables import getRows

import tkinter as tk


class Base:
    pass

class Top(Base):
    pass


print(getBaseClasses(True))

print(isinstance(True, object))
