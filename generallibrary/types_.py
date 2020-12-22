

def strToDynamicType(var):
    """
    Try to convert a string to bool, None, int or float.
    If failed then it returns the given var.

    :param any var: Object to be converted
    :return: Converted string or original string if failed
    :raises TypeError: If var is not a string
    """
    var = str(var)

    keyWords = {"true": True, "false": False, "none": None}
    if var.lower() in keyWords:
        return keyWords[var.lower()]

    # int() doesn't declare 'raises' in doc type so catch everything
    try:
        return int(var)
    except (ValueError, TypeError):
        pass

    # float() doesn't declare 'raises' in doc type so catch everything
    try:
        return float(var)
    except (ValueError, TypeError):
        pass

    return var

def _typeChecker_checkObject(obj, types, literalObjects):
    objDepth = depth(obj)
    typesDepth = len(types) - 1
    if objDepth != typesDepth:
        raise TypeError(f"Obj depth {objDepth} doesnt match types depth {typesDepth}")

    for i, typeTuple in enumerate(types):
        # Returned ValueError if obj was pandas.DataFrame, so there are probably more objects that can raise any error
        # So catch every exception, it's a pretty simple statement so not too big of a problem
        for literalObj in literalObjects:
            if obj is literalObj:
                objInLiteralObjects = True
                break
        else:
            objInLiteralObjects = False

        if objInLiteralObjects:
            if obj not in typeTuple:
                raise TypeError(f"obj {obj} was a literal object in {literalObjects} but not in {typeTuple} in depth {i}/{typesDepth}")
        else:
            typeTupleWithoutLiteralObjects = tuple([t for t in typeTuple if t not in literalObjects])
            typeTupleWithOnlyTypes = tuple([t for t in typeTupleWithoutLiteralObjects if not isinstance(t, str)])
            typeTupleWithOnlyStrings = tuple([t for t in typeTuple if isinstance(t, str)])

            objTypeInList = isinstance(obj, typeTupleWithOnlyTypes)

            objClassNameInList = False
            for className in getBaseClassNames(obj, includeSelf=True):
                if isinstance(obj, bool) and className == "int":
                    continue
                if className in typeTupleWithOnlyStrings:
                    objClassNameInList = True
                    break

            # Because isinstance(False, int) = True
            isBoolAndBoolOrObjectNotInList = isinstance(obj, bool) and bool not in typeTupleWithOnlyTypes and object not in typeTupleWithOnlyTypes and not objClassNameInList

            if isBoolAndBoolOrObjectNotInList or not (objTypeInList or objClassNameInList):
                raise TypeError(f"obj {obj} wasn't type {typeTuple} in depth {i}/{typesDepth}")

        if isIterable(obj):
            obj = iterFirstValue(obj)
        elif i < objDepth:
            raise TypeError(f"obj {obj} is not iterable but atleast one more subtype is required in depth {i}/{typesDepth}")

def _typeChecker_prepareTypesList(types, literalObjects):
    newTypes = []
    for argType in types:
        if isinstance(argType, (list, tuple, set)):
            newArgType = list(argType)
        else:
            isType = isinstance(argType, type)
            isLiteralObject = argType in literalObjects
            isNameOfClass = isinstance(argType, str)
            if isType or isLiteralObject or isNameOfClass:
                newArgType = [argType]
            else:
                raise TypeError(f"Argument type {argType} is not a list, tuple, set, type or literalObject")


        newArgTypeWithOnlyStrings = tuple([t for t in newArgType if isinstance(t, str)])
        floatInList = float in newArgType or "float" in newArgTypeWithOnlyStrings
        intInList = int in newArgType or "int" in newArgTypeWithOnlyStrings

        if floatInList and not intInList:
            newArgType.append(int)

        newTypes.append(tuple(newArgType))
    return newTypes

def typeChecker(obj, *types, error=True):
    """
    Check type(s) of an object.
    The first type correlates to the first layer of obj and so on.
    Each type can be a (tuple that holds) type, string or literal object such as `None`.

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


def getBaseClasses(obj, includeSelf=False, includeObject=True):
    """
    Get all base classes from an object's class.

    :param any obj: Generic obj or class
    :param includeSelf: Whether to include own class or not
    :param includeObject: Whether to include object class or not (Every object has object as base)
    :return: List of classes
    :rtype: list[type]
    """
    if isinstance(obj, type):
        cls = obj
    else:
        cls = obj.__class__

    classes = list(cls.__bases__)
    for base in classes:
        for baseClassBase in getBaseClasses(base):
            if baseClassBase not in classes:
                classes.append(baseClassBase)

    if includeSelf:
        classes.insert(0, cls)

    if not includeObject:
        classes.remove(object)

    return classes


def getBaseClassNames(obj, includeSelf=False):
    """
    Get all base classes from an object's class.

    :param any obj: Generic obj or class
    :param includeSelf: Whether to include own class name or not
    :return: List of lowered class names
    :rtype: list[str]
    """
    return [cls.__name__ for cls in getBaseClasses(obj, includeSelf)]


def hasMethod(obj, method):
    """
    Return whether an object has a specific callabale attribute.

    :param object obj: Any object
    :param str method: String of method to check
    """
    attr = getattr(obj, method, False)
    return attr and callable(attr)


class HierarchyStorer(type):
    """ A metaclass that automatically stores references to all inheriters.
        By inheritence each inheriter gets it too.

        Example:
            class Base(metaclass=HierarchyStorer, base="Base"):
            class A(Base):
            class B(A):

            Defines Base.A, Base.B, A.Base, B.Base
            """
    _base_name = ...

    def __new__(mcs, name, bases, clsdict, base=None):
        if base is not None:
            mcs._base_name = base
        return type.__new__(mcs, name, bases, clsdict)

    def __init__(cls, name, bases, clsdict, *_, **__):
        base_cls = [base for base in getBaseClasses(cls, includeSelf=True) if base.__name__ == cls._base_name][0]
        setattr(base_cls, name, cls)
        type.__init__(cls, name, bases, clsdict)

        # Store all inheriters (including base_cls) in a list in base_cls. Todo: TnD
        if getattr(base_cls, "_inheriters", None) is None:
            base_cls._inheriters = []
        base_cls._inheriters.append(cls)


from generallibrary.iterables import depth, iterFirstValue, isIterable
