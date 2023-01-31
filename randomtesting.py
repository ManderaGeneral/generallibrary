from functools import partial

from generallibrary import *


# print(depth("hi"))
# print(depth({"hi": "there"}))
# print(depth({'test': {'foo': 'bar', 'number': 2, 'hi': ['a', 'b', 3], "uh": None}}))



# print(Terminal("-c", "print(5)", python=True, error=False, capture_output=False))

print(Terminal("-c", "assert 4 == 5", python=True, capture_output=True, error=False).string_result)
