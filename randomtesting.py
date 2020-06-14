
from generallibrary.time import *
from generallibrary.types import *
from generallibrary.iterables import *
from generallibrary.functions import *

import tkinter as tk

import inspect

import random

class Class:
    def __init__(self):
        self.test = 1

    @property
    def test(self):
        return self._test

print(Class.test())
