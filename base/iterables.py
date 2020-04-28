
def iterable(obj):
    if isinstance(obj, tuple):
        return obj
    elif isinstance(obj, list):
        return obj
    elif isinstance(obj, dict):
        return obj.values()
    else:
        return None

def depth(obj):
    depth = 0
    while True:
        if iterable(obj):
            obj = iterFirstValue(obj)
            depth += 1
        else:
            return depth

def dictFirstValue(dictionary):
    if not isinstance(dictionary, dict):
        raise TypeError("Not dictionary")
    if not len(dictionary):
        return None
    return dictionary[list(dictionary.keys())[0]]

def iterFirstValue(obj):
    if not iterable(obj):
        raise TypeError("obj is not iterable")
    if isinstance(obj, tuple) or isinstance(obj, list):
        return obj[0]
    elif isinstance(obj, dict):
        return dictFirstValue(obj)
