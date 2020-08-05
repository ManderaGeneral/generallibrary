
from generallibrary.time import *
from generallibrary.types import *
from generallibrary.iterables import *
from generallibrary.functions import *
from generallibrary.object import *
from generallibrary.values import *

# from generalobjexp import ObjExp





# class Base:
#     def __init__(self, x):
#         self.x = x
#
# @initBases
# class Parent(Base):
#     def __init__(self, x):
#         self.y = 2
#
#
# Parent()
# print(SigInfo(Parent).validParameters())


sigInfo = SigInfo(lambda x, *args, y=2, **kwargs: 5, args=(1, 5), kwargs={"x": 2, "z": 4})
# sigInfo = SigInfo(lambda x, *args, y=2, **kwargs: debug(locals()), args=(1, 5), kwargs={"x": 2, "z": 4})

# class Test:
#     def __init__(self, x):
#         print(x)
# sigInfo = SigInfo(Test, args=(5,))

print(sigInfo.args, sigInfo.kwargs)
sigInfo["args"] = [6, 7]
print(sigInfo.args, sigInfo.kwargs)

sigInfo.validParameters()
sigInfo()




