
from generallibrary.time import *
from generallibrary.types import *
from generallibrary.iterables import *
from generallibrary.functions import *

import tkinter as tk

import inspect

import random

# HERE ** Make this work
def wrapper(func):
    def f(*args, **kwargs):
        changeParameter(hello, kwargs, args, "x", 4)
        return func(*args, **kwargs)
    return f

@wrapper
def hello(x, y=5):

    print(x, y)


hello(2)


