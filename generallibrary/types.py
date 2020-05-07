


def strToDynamicType(var):
    """
    Try to convert a string to bool, None, int or float.
    If failed then it returns the given var.

    :param str var: String object to be converted
    :return: Converted string or original string if failed
    :raises TypeError: If var is not a string
    """
    if not isinstance(var, str):
        raise TypeError(f"var {var} is not a string")

    keyWords = {"true": True, "false": False, "none": None}
    if var.lower() in keyWords:
        return keyWords[var.lower()]

    # int() doesn't declare 'raises' in doc type so catch everything
    try:
        return int(var)
    except:
        pass

    # float() doesn't declare 'raises' in doc type so catch everything
    try:
        return float(var)
    except:
        pass

    return var



def _typeChecker_checkObject(obj, types, literalObjects):
    objDepth = depth(obj)
    typesDepth = len(types) - 1
    if objDepth != typesDepth:
        raise TypeError(f"Obj depth {objDepth} doesnt match types depth {typesDepth}")

    for i, argType in enumerate(types):
        # Returned ValueError if obj was pandas.DataFrame, so there are probably more objects that can raise any error
        # So catch every exception, it's a pretty simple statement so not too big of a problem
        try:
            objInLiteralObjects = obj in literalObjects
        except:
            objInLiteralObjects = False

        if objInLiteralObjects:
            if obj not in argType:
                raise TypeError(f"obj {obj} was a literal object but not in literalObjects list {literalObjects} in depth {i}/{typesDepth}")
        else:
            argTypeWithoutLiteralObjects = tuple([singleType for singleType in argType if singleType not in literalObjects])
            isArgType = isinstance(obj, argTypeWithoutLiteralObjects)
            isBoolAndBoolNotInArgType = isinstance(obj, bool) and bool not in argType  # Because isinstance(False, int) = True

            if not isArgType or isBoolAndBoolNotInArgType:
                raise TypeError(f"obj {obj} wasn't type {argType} in depth {i}/{typesDepth}")

        if iterable(obj):
            obj = iterFirstValue(obj)
        elif i < objDepth:
            raise TypeError(f"obj {obj} is not iterable but atleast one more subtype is required in depth {i}/{typesDepth}")

def _typeChecker_prepareTypesList(types, literalObjects):
    newTypes = []
    for argType in types:
        if isinstance(argType, (list, tuple)):
            newArgType = list(argType)
        else:
            isType = isinstance(argType, type)
            isLiteralObject = argType in literalObjects
            if isType or isLiteralObject:
                newArgType = [argType]
            else:
                raise TypeError(f"Argument type {argType} is not a list, tuple, type or literalObject")

        if float in newArgType and int not in newArgType:
            newArgType.append(int)
        newTypes.append(tuple(newArgType))
    return newTypes

def typeChecker(obj, *types, error=True):
    """
    Check types of an obj. Intended for iterables with somewhat consistent structure in every layer.
    The first type correlates to the first layer of obj and so on.

    :param obj: Generic obj, iterable or not
    :param types: lists or tuples if obj at that level can be multiple types, single type if only one
    :param error: Raise error if true, otherwise returns False when fail
    :return:
    """
    literalObjects = [None]
    try:
        if not types:
            raise TypeError("No types were given as args")

        types = _typeChecker_prepareTypesList(types, literalObjects)
        _typeChecker_checkObject(obj, types, literalObjects)

    except TypeError as e:
        if error:
            raise e
        else:
            return False
    else:
        return True



from generallibrary.iterables import depth, iterFirstValue, iterable
