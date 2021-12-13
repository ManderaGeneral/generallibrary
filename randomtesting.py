from generallibrary import *

from dill import loads, dumps, DEFAULT_PROTOCOL
# from pickle import loads, dumps


class X(Recycle):
    _recycle_keys = {"y": str}

    def __init__(self, y):
        self.y = y

    def __repr__(self):
        return f"{self.y}: {id(self)}"

    # def __reduce__(self):
    #     return X, (2, )

    # def __getstate__(self):
    #     state = self.__dict__.copy()
    #     print(state)
    #     state.pop("_recycle_is_new", None)
    #     return state

    # def __setstate__(self, state):
    #     print(state)
    #     self.__dict__ = state

    # def __getnewargs__(self):
    #     return self.y,



a = X(2)
b = X(2)

print(a, b)

a2 = loads(dumps(a, protocol=5), ignore=True)
b2 = loads(dumps(b, protocol=5), ignore=True)

print(a2, b2)



