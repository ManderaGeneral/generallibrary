
from generallibrary import *
from collections import ChainMap

class C(Recycle):
    _recycle_keys = {"x": str}

    def __init__(self, x):
        pass

print(C(1) is C(2))

# all_recycle_keys = get_attrs_from_bases(C, "_recycle_keys", ignore=None)
# recycle_keys = ChainMap(*all_recycle_keys)
#
# sigInfo["cls"] = C
# recycle_list = [sigInfo.call(func) for name, func in recycle_keys.items()]
#
# print(recycle_list)
