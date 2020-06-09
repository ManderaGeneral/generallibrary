
from generallibrary.time import *
from generallibrary.types import *
from generallibrary.iterables import *
from generallibrary.functions import *

import tkinter as tk

import inspect

import random

def wrapper(func):
    def f(*args, **kwargs):
        # args, kwargs = changeArgsAndKwargs(func, args, kwargs, x=2)
        print(getParameter(func, args, kwargs, "x"))
        return func(*args, **kwargs)
    return f

@wrapper
def hello(x, y=5):

    print(x, y)

hello(2)


