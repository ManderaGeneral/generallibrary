

class SortedList:
    """
    Controls a sorted list in ascending order.
    """
    def __init__(self, *objects, getValueFunc=None):
        """
        :param objects: Objects to be added instantly
        :param function[any] -> float getValueFunc: A function that only takes obj as parameter and returns a float to be used for sorting.
        """
        if objects and typeChecker(objects[0], "function", error=False):
            raise AttributeError("First object was a function, make sure to use the 'getValueFunc' key.")

        if getValueFunc is None:
            getValueFunc = lambda obj: obj

        self.getValueFunc = getValueFunc
        self.objects = []
        self._values = []
        self.add(*objects)

    def __repr__(self):
        return f"<SortedList: {self.objects}>"

    def __contains__(self, item):
        return item in self.objects

    def __iter__(self):
        return self.objects.__iter__()

    def add(self, *objects):
        """
        Add objects to sorted list.
        """
        for newObj in objects:
            newValue = self.getValueFunc(newObj)
            for i, obj in enumerate(self.objects):
                value = self._values[i]
                if newValue <= value:
                    index = i
                    break
            else:
                index = len(self.objects)

            self.objects.insert(index, newObj)
            self._values.insert(index, newValue)

    def remove(self, *objects):
        """
        Remove objects from sorted list.
        """
        for removeObj in objects:
            if removeObj not in self.objects:
                continue

            index = self.objects.index(removeObj)
            del self.objects[index]
            del self._values[index]

def getIterable(obj):
    """
    Returns the iterable values of a tuple, list or dict. Otherwise `False`.
    Can be used for typechecking or iterating generic obj.

    Wrong way
    ---------
    >>> not getIterable(5)
    >>> True
    >>> not getIterable([])
    >>> True

    Right way
    ---------
    >>> getIterable(5) is False
    >>> True
    >>> getIterable([]) is False
    >>> False

    :param obj: Generic obj
    :return: Iterable list
    """
    if isinstance(obj, tuple):
        return list(obj)
    elif isinstance(obj, list):
        return obj
    elif isinstance(obj, dict):
        return list(obj.values())
    else:
        return False

def isIterable(obj):
    """
    See if an obj is a tuple, list or dict.

    :param obj: Generic obj
    :rtype: bool
    """
    return getIterable(obj) is not False

def depth(obj):
    """
    Get depth of an object by recursively checking the first value.

    :param obj: Generic obj
    """
    depth = 0
    while True:
        if getIterable(obj):
            obj = iterFirstValue(obj)
            depth += 1
        else:
            return depth

def dictFirstValue(dictionary):
    """
    Get first 'random' value of a dictionary or None.

    :param dict dictionary: Generic dictionary
    :raises TypeError: If not dictionary
    """
    if not isinstance(dictionary, dict):
        raise TypeError("Not dictionary")

    if not dictionary:
        return None

    return dictionary[list(dictionary.keys())[0]]

def iterFirstValue(obj):
    """
    Get first 'random' value of an iterable or None.

    :param obj: Generic iterable
    :raises TypeError: If not iterable
    """
    if isIterable(obj) is False:
        raise TypeError("obj is not iterable")

    if isinstance(obj, tuple) or isinstance(obj, list):
        if not obj:
            return None
        else:
            return obj[0]
    elif isinstance(obj, dict):
        return dictFirstValue(obj)

def joinWithStr(delimeter, obj):
    """
    Like str.join() but it casts the values to strings first, also takes dict.

    :param obj: Generic iterable
    :param str delimeter: String to be put between values
    :raises TypeError: If obj is not iterable
    :return: A string containing values of obj with delimeter between each
    """
    iterable = getIterable(obj)
    if iterable is False:
        raise TypeError(f"{obj} is not iterable")

    return delimeter.join([str(value) for value in iterable])

def addToListInDict(dictionary, key, *args):
    """
    Add a value to a list inside a dictionary, automatically creates list.
    Since list is mutable we can change dictionary directly.

    :param dict dictionary:
    :param key:
    :return: Updated given dictionary
    """
    assert isinstance(dictionary, dict)
    if key in dictionary:
        assert isinstance(dictionary[key], list)
    else:
        dictionary[key] = []

    dictionary[key].extend(args)
    return dictionary

def addToDictInDict(dictionary, key, **kwargs):
    """
    Add a key-value argument to a dict inside a dict, automatically creates dict.

    :param dict dictionary:
    :param key:
    :return: Updated given dictionary
    """
    assert isinstance(dictionary, dict)
    if key in dictionary:
        assert isinstance(dictionary[key], dict)
    else:
        dictionary[key] = {}

    dictionary[key].update(kwargs)
    return dictionary

def getFreeIndex(dictionary):
    """
    Get the first free integer index of dictionary starting at 0.

    :param dict dictionary:
    """
    index = 0
    while True:
        if index in dictionary:
            index += 1
        else:
            return index


def appendToDict(dictionary, obj):
    """
    Puts an object in the lowest free integer index and returns index.
    Useful for returning an index that wont change, unlike a list.
    Keys can be deleted using the returned index without affecting other values.

    :param dict dictionary:
    :param any obj:
    :return: Used index
    """
    index = getFreeIndex(dictionary)
    dictionary[index] = obj
    return index


def dict_index(dict_, match, default=(sentinel := object())):
    """ Get the first match' index. """
    try:
        return next(key for key, value in dict_.items() if value == match)
    except StopIteration as e:
        if default is sentinel:
            raise e
        else:
            return default

def _getRows_getRow(iterableObj, key=None):
    """
    Takes an object and returns a list of rows to use for appending.

    :param iterableObj: Iterable
    :param key: If iterableObj had a key to assigned it it's given here
    :return: A
    """
    row = [key] if key else []
    if isinstance(iterableObj, (list, tuple)):
        row.extend(iterableObj)
    elif isinstance(iterableObj, dict):
        for _, value in sorted(iterableObj.items()):
            row.append(value)
    return row

def getRows(obj):
    """
    Get rows as lists in list from a tuple, list or dict (where it discards keys).
    All these objects result in [[1, 2, 3], [4, 5, 6]]
     | [[1, 2, 3], [4, 5, 6]]
     | [{"a": 1, "b": 2, "c": 3}, {"d": 4, "e": 5, "f": 6}]
     | {1: {"b": 2, "c": 3}, 4: {"e": 5, "f": 6}}
     | {1: [2, 3], 4: [5, 6]}

    :param any obj: Iterable (Optionally inside another iterable) or a value for a single cell
    :return:
    """
    rows = []
    if obj is None:
        return rows
    if isIterable(obj):
        if not len(obj):
            return rows

        if isinstance(obj, (list, tuple)):
            if isIterable(obj[0]):
                for subObj in obj:
                    rows.append(_getRows_getRow(subObj))
            else:
                rows.append(_getRows_getRow(obj))
        elif isinstance(obj, dict):
            if isIterable(dictFirstValue(obj)):
                for key, subObj in obj.items():
                    rows.append(_getRows_getRow(subObj, key))
            else:
                rows.append(_getRows_getRow(obj))
    else:
        rows.append([obj])
    return rows

def exclusive(dictionary, *keys):
    """
    Returns a new dictionary without keys.

    :param dict dictionary:
    :param keys: Keys to be exluded.
    """
    return {key: value for key, value in dictionary.items() if key not in keys}

def inclusive(dictionary, *keys):
    """
    Returns a new dictionary without keys not in keys.

    :param dict dictionary:
    :param keys: Keys to include
    """
    return {key: value for key, value in dictionary.items() if key in keys}

def uniqueObjInList(l, obj, active):
    """
    Controls whether a unique object should be present in a list.
    Adds obj to list if active and obj isn't in list.
    Removes obj from list if not active and obj in list.
    Changes list directly because of mutable.

    :param list l:
    :param any obj:
    :param bool active:
    """
    if active:
        if obj not in l:
            l.append(obj)
    else:
        if obj in l:
            l.remove(obj)

def remove_duplicates(l):
    """ Remove all duplicates in a list.
        Values must be hashable as they are passed through as dict keys. (Lists work but not Dicts) """
    return list(dict.fromkeys(l))
    # return list(set(l))

def combine(**kwargs):
    """
    Create a list of dicts containing every unique combination from given object (Can be tuples).
    """
    execLines = []
    for i, (key, value) in enumerate(kwargs.items()):
        execLines.append(f"{' ' * i * 4}for {key} in (kwargs['{key}'] if isIterable(kwargs['{key}']) else [kwargs['{key}']]):")
    lines = [f"'{key}': {key}" for key in list(kwargs.keys())]
    execLines.append(f"{' ' * len(kwargs) * 4}combinations.append({{{', '.join(lines)}}})")

    combinations = []
    exec("\n".join(execLines))
    return [] if combinations == [{}] else combinations

from generallibrary.types_ import typeChecker








































































