
import itertools


class SortedList:
    """
    Controls a sorted list in ascending order.
    """
    def __init__(self, *objects, getValueFunc=None):
        """
        :param objects: Objects to be added instantly
        :param function[any] -> float getValueFunc: A function that only takes obj as parameter and returns a float to be used for sorting.
        """

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


def get_keys(obj):
    """ Returns an iterator or iterable containing keys of given obj. """
    if hasattr(obj, "keys"):
        return obj.keys()
    else:
        return range(len(obj))


def get_values(obj):
    """ Returns an iterator or iterable containing values of given obj. """
    if hasattr(obj, "values"):
        return obj.values()
    else:
        return iter(obj)


def get_items(obj):
    """ Returns an iterator which yields both key and value for any iterable. """
    if hasattr(obj, "items"):
        return obj.items()
    else:
        return enumerate(obj)


def is_iterable(obj):
    """ Get whether an obj is iterable. """
    return hasattr(obj, "__iter__")


def depth(obj):
    """ Get depth of an object by recursively checking the first value. """
    sentinel = object()
    depth = 0
    while True:
        if not is_iterable(obj=obj):
            break
        first_value = iter_first_value(iterable=obj, default=sentinel)
        if first_value == obj or first_value is sentinel:
            break
        obj = first_value
        depth += 1
    return depth


def iter_first_value(iterable, default=None):
    """ Get first 'random' value of an iterable or default value. """
    for x in iterable:
        if hasattr(iterable, "values"):
            return iterable[x]
        else:
            return x

    return default


def join_with_str(delimiter, obj):
    """ Like str.join() but it casts the values to strings first, also takes dict. """
    return delimiter.join([str(value) for value in get_values(obj)])


def extend_list_in_dict(dictionary, key, *args):
    """ Add a value to a list inside a dictionary, automatically creates list. """
    assert isinstance(dictionary, dict)
    if key in dictionary:
        assert isinstance(dictionary[key], list)
    else:
        dictionary[key] = []

    dictionary[key].extend(args)
    return dictionary


def update_dict_in_dict(dictionary, key, **kwargs):
    """ Add a key-value argument to a dict inside a dict, automatically creates dict. """
    assert isinstance(dictionary, dict)
    if key in dictionary:
        assert isinstance(dictionary[key], dict)
    else:
        dictionary[key] = {}

    dictionary[key].update(kwargs)
    return dictionary


def get_free_index(dictionary):
    """ Get the first free integer index of dictionary starting at 0. """
    index = 0
    while True:
        if index in dictionary:
            index += 1
        else:
            return index


def append_to_dict(dictionary, obj):
    """ Puts an object in the lowest free integer index and returns index.
        Useful for returning an index that wont change, unlike a list.
        Keys can be deleted using the returned index without affecting other values.

        :return: Used integer index. """
    index = get_free_index(dictionary)
    dictionary[index] = obj
    return index


def get(iterable, index=None, default=None):
    """ Get value of an iterable by index, mainly lists, tuples and sets that don't have a `get` method, works for dict too.
        Returns first random value if set, returns default value if not found. """
    if isinstance(iterable, set):
        try:
            return next(iter(iterable))
        except StopIteration:
            return default
    else:
        try:
            return iterable[index]
        except (IndexError, KeyError):
            return default


def get_index(iterable, match, default=...):
    """ Get the first match' index.
        If not found it returns default value if specified, otherwise raises ValueError. """
    try:
        return next(key for key, value in get_items(iterable) if value == match)
    except StopIteration as e:
        if default is Ellipsis:
            raise ValueError(f"{match} was not found in {iterable}")
        else:
            return default


def remove(iterable, match):
    """ Remove member of an iterable, works for dict, list and set.
        Returns True if removed, False if not found. """
    if isinstance(iterable, set):
        try:
            iterable.remove(match)
        except KeyError:
            return False
        else:
            return True
    else:
        index = get_index(iterable, match, sentinel := object())
        if index is sentinel:
            return False
        else:
            del iterable[index]
            return True



def _get_rows_helper(iterableObj, key=None):
    """ Takes an object and returns a list of rows to use for appending.

        :param iterableObj: Iterable
        :param key: If iterableObj had a key to assigned it it's given here """
    row = [key] if key else []
    if isinstance(iterableObj, (list, tuple)):
        row.extend(iterableObj)
    elif isinstance(iterableObj, dict):
        for _, value in sorted(iterableObj.items()):
            row.append(value)
    return row


def get_rows(obj):
    """ Get rows as lists in list from a tuple, list or dict (where it discards keys).
        All these objects result in [[1, 2, 3], [4, 5, 6]]
         | [[1, 2, 3], [4, 5, 6]]
         | [{"a": 1, "b": 2, "c": 3}, {"d": 4, "e": 5, "f": 6}]
         | {1: {"b": 2, "c": 3}, 4: {"e": 5, "f": 6}}
         | {1: [2, 3], 4: [5, 6]}

        :param any obj: Iterable (Optionally inside another iterable) or a value for a single cell """
    rows = []
    if obj is None:
        return rows
    if is_iterable(obj):
        if not len(obj):
            return rows

        if isinstance(obj, (list, tuple)):
            if is_iterable(obj[0]):
                for subObj in obj:
                    rows.append(_get_rows_helper(subObj))
            else:
                rows.append(_get_rows_helper(obj))
        elif isinstance(obj, dict):
            if is_iterable(iter_first_value(obj)):
                for key, subObj in obj.items():
                    rows.append(_get_rows_helper(subObj, key))
            else:
                rows.append(_get_rows_helper(obj))
    else:
        rows.append([obj])
    return rows


def exclusive(dictionary, *keys):
    """ Returns a new dictionary without keys. """
    return {key: value for key, value in dictionary.items() if key not in keys}


def inclusive(dictionary, *keys):
    """ Returns a new dictionary with keys. """
    return {key: value for key, value in dictionary.items() if key in keys}


def unique_obj_in_list(list_, obj, active):
    """ Controls whether a unique object should be present in a list.
        Adds obj to list if active and obj isn't in list.
        Removes obj from list if not active and obj in list. """
    if active:
        if obj not in list_:
            list_.append(obj)
    else:
        if obj in list_:
            list_.remove(obj, )

def remove_duplicates(list_, func=None):
    """ Remove all duplicates in a list.
        Set func to use another value than a self hash for determining if duplicate.
        Values must be hashable (If func is None) as they are passed through as dict keys. (Lists work but not Dicts) """
    if func is None:
        return list(dict.fromkeys(list_))
    else:
        return list({func(obj): obj for obj in list_}.values())

def combine(**kwargs):
    """ Create a list of dicts containing every unique combination from given kwargs.
        Values can be iterable or not. """
    execLines = []
    for i, (key, value) in enumerate(kwargs.items()):
        execLines.append(f"{' ' * i * 4}for {key} in (kwargs['{key}'] if is_iterable(kwargs['{key}']) else [kwargs['{key}']]):")
    lines = [f"'{key}': {key}" for key in list(kwargs.keys())]
    execLines.append(f"{' ' * len(kwargs) * 4}combinations.append({{{', '.join(lines)}}})")

    combinations = []
    exec("\n".join(execLines))
    return [] if combinations == [{}] else combinations

def split_list(func, *args):
    """ Split args into one list containing all args where func returned True, and rest in the second one. """
    one, two = [], []
    for arg in args:
        if func(arg):
            one.append(arg)
        else:
            two.append(arg)
    return one, two

def pivot_list(list_, index):
    """ Return a new altered list where it's first value is the given index for the original list. """
    index %= len(list_)
    return list_[index:] + list_[:index]

def flatten(list_, gen=False):
    """ Flatten a list. """
    if gen:
        return itertools.chain(*list_)
    else:
        return list(flatten(list_=list_, gen=True))

def subtract_list(a, b):
    """ Returns a new list with elements in b removed from a. """
    a = a.copy()
    for x in b:
        if x in a:
            a.remove(x)
    return a

def dict_insert(dict_, **kwargs):
    """ Update a dict with new values as normal, except their insertion order will be first.
        Warning: This could potentially be slow, it also duplicates entire dict in memory. """
    kwargs.update(dict_)
    dict_.clear()
    dict_.update(kwargs)

































