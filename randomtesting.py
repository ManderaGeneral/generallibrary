from functools import partial

from generallibrary import *


# print(depth("hi"))
# print(depth({"hi": "there"}))
# print(depth({'test': {'foo': 'bar', 'number': 2, 'hi': ['a', 'b', 3], "uh": None}}))


# print(type(terminal("-c", "assert False", python=True)))

# print(Terminal("-c", "print(5)", python=True, error=False, capture_output=False).success())

# Maybe terminal could be a class instead?


from subprocess import CalledProcessError