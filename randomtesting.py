
from generallibrary.time import *
from generallibrary.types import *
from generallibrary.iterables import *
from generallibrary.functions import *
from generallibrary.object import *
from generallibrary.values import *
from generallibrary.versions import *

# from generalobjexp import ObjExp

import sys

# print(str(sys.version_info.releaselevel))

# print(VerInfo().pythonString)



# from packaging import version
# print(sys.version_info)

# import sys
# for name, module in sorted(sys.modules.items()):
#     if hasattr(module, '__version__'):
#         print(name, module.__version__ )
#
# ver = VerInfo()

# print(ObjExp.__module__)




# print(version.parse(VerInfo().pythonString) == version.parse("3.7"))
print(VerInfo().pythonVersion != "3.8.00")


# print(VerInfo().pythonVersion == "3.8")




# from pip._internal.utils.misc import get_installed_distributions
# ObjExp(get_installed_distributions(), showDunders=True)