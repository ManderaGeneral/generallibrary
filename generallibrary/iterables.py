
def iterable(obj):
    """
    Returns the iterable values of an object or False.
    Can be used for typechecking or iterating generic obj.

    Wrong way
    ---------
    >>> not iterable(5)
    >>> True
    >>> not iterable([])
    >>> True

    Right way
    ---------
    >>> iterable(5) is False
    >>> True
    >>> iterable([]) is False
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

def depth(obj):
    """
    Checks depths of an obj by keep going to the first value of obj.

    :param obj: Generic obj
    """
    depth = 0
    while True:
        if iterable(obj):
            obj = iterFirstValue(obj)
            depth += 1
        else:
            return depth

def dictFirstValue(dictionary):
    """
    Get first 'random' value of a dictionary.

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
    Get first 'random' value of an iterable.

    :param obj: Generic iterable
    :raises TypeError: If not iterable
    """
    if iterable(obj) is False:
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
    Like str.join() but it casts the values to strings first.

    :param obj: Generic iterable
    :param str delimeter: String to be put between values
    :raises TypeError: If obj is not iterable
    :return: A string containing values of obj with delimeter between each
    """
    if not (obj := iterable(obj)):
        raise TypeError("obj is not iterable")

    return delimeter.join([str(value) for value in obj])










