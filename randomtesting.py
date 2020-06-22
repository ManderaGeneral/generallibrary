
from generallibrary.time import *
from generallibrary.types import *
from generallibrary.iterables import *
from generallibrary.functions import *

import tkinter as tk

import inspect

import random


def attributeMatch(attribute, dataList, filter):
    returnList = []
    count = 0

    occurence = attribute.count('.')
    nest = {}  # Used to hold dynamic variables
    dot = '.'

    for entry in dataList:
        # If attribute contains . meaning nested object
        if '.' in attribute:
            attribute.split('.')
            for i in range(occurence + 1):
                nest['atr%d' % i] = attribute.split('.')[i]

            currentAttr = entry[nest['atr0']]
            for i in range(occurence):
                currentAttr = currentAttr[nest[f'atr{i + 1}']]
                if filter not in currentAttr:
                    count += 1
                    returnList.append(entry)

    return count, returnList
