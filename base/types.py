
def strToDynamicType(var):
    if var == "true" or var == "True":
        return True
    if var == "false" or var == "False":
        return False

    try:
        return int(var)
    except:
        pass

    try:
        return float(var)
    except:
        pass

    return var


def typeChecker(obj, *types, fullIteration=False, raiseTypeError=True):
    """
    Check types of an obj. Intended for iterables with somewhat consistent structure in every layer.
    :param obj:
    :param types:
    :param fullIteration:
    :param raiseTypeError:
    :return:
    """
    try:
        if not types:
            raise TypeError("No types were given as args")
        objDepth = depth(obj)
        typesDepth = len(types) - 1
        if objDepth != typesDepth:
            raise TypeError(f"Obj depth {objDepth} doesnt match types depth {typesDepth}")

        for i, argType in enumerate(types):
            if not isinstance(obj, argType):
                raise TypeError(f"obj {obj} wasn't type {argType} in depth {i}/{typesDepth}")

            if iterable(obj):
                obj = iterFirstValue(obj)
            elif i < objDepth:
                raise TypeError(f"obj {obj} is not iterable but atleast one more subtype is required in depth {i}/{typesDepth}")

    except TypeError as e:
        if raiseTypeError:
            raise e
        else:
            return False
    else:
        return True



from base.iterables import depth, iterFirstValue, iterable
