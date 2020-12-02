
import sys
from types import ModuleType, FunctionType, MethodWrapperType
from gc import get_referents
import inspect



_BLACKLIST = type, ModuleType, FunctionType
def getsize(obj):
    """
    Get a sum of sizes from an object and it's members in bytes.
    Custom objects know their class.
    Function objects seem to know way too much, including modules.
    Exclude modules as well.

    Author: Aaron Hall @ https://stackoverflow.com/questions/449560/how-do-i-determine-the-size-of-an-object-in-python
    """
    if isinstance(obj, _BLACKLIST):
        # raise TypeError('getsize() does not take argument of type: '+ str(type(obj)))
        return sys.getsizeof(obj)
    seen_ids = set()
    size = 0
    objects = [obj]
    while objects:
        need_referents = []
        for obj in objects:
            if not isinstance(obj, _BLACKLIST) and id(obj) not in seen_ids:
                seen_ids.add(id(obj))
                size += sys.getsizeof(obj)
                need_referents.append(obj)
        objects = get_referents(*need_referents)
    return size

# HERE ** Put this in ObjInfo
def attributes(obj, properties=True, class_=True, methods=True, variables=True, modules=False, protected=False, from_instance=True, from_class=True, from_bases=True):
    """ Get attributes from a Module or Class with a lot of optional flags for filtering.

        :param obj:
        :param bool properties:
        :param bool class_:
        :param bool methods:
        :param bool variables:
        :param bool modules:
        :param bool or None protected: Whether to return protected, non-protected or all if None.
        :param bool from_instance: Whether to return attributes only defined in instance.
        :param bool from_class: Whether to return attributes defined in direct class.
        :param bool from_bases: Whether to return attributes defined by an inheritence. """
    if isinstance(obj, type):
        cls = obj
        instance = None
    else:
        cls = obj.__class__
        instance = obj

    attrs = {}
    for key in dir(obj):
        cls_attr = getattr(cls, key, NotImplemented)
        is_property = isinstance(cls_attr, property)
        is_protected = key.startswith("_")
        attr = cls_attr if is_property else getattr(obj, key, NotImplemented)

        # Attribute is Property, Method and Variable
        if is_property:
            if properties is False:
                continue
        elif inspect.isclass(attr):
            if class_ is False:
                continue
        elif callable(attr):
            if methods is False:
                continue
        elif cls.__name__ == "module":
            if modules is False:
                continue
        else:
            if variables is False:
                continue

        # Key is Protected
        if protected is False and is_protected:
            continue
        elif protected is True and not is_protected:
            continue

        # Origin from Instance, Class, Base or Builtin
        if from_instance is False and instance and attr != cls_attr and cls_attr is NotImplemented:
            continue
        elif not (from_class and from_bases) and cls_attr is not NotImplemented:
            for base in cls.__bases__:
                if getattr(base, key, NotImplemented) is not NotImplemented:
                    defined_in_base = True
                    break
            else:
                defined_in_base = False

            if from_bases is False and defined_in_base:
                continue
            elif from_class is False and not defined_in_base:
                continue

        attrs[key] = attr
    return attrs

def initBases(cls):
    """
    Decorator function for class to automatically initalize all inherited classes.

    Wrap a class' unbound __init__ method to take any arguments.
    When wrapper is called it iterates DIRECT bases to call their unbound __init__ methods along with it's own original __init__.

    Also looks for defined `_post_init` methods, stores them in `instance._post_inits` and calls them all after all inits.
    """
    cls_init = cls.__init__  # Unbound original __init__ method of class

    print("here", cls)
    cls._is_wrapped_by_initBases = cls

    def _wrapper(*args, **kwargs):
        cls_SigInfo = SigInfo(cls_init, *args, **kwargs)

        if not cls_SigInfo["self"]:
            raise AttributeError(f"{cls} hasn't defined it's `__init__`")

        initialized_bases = []

        if getattr(cls_SigInfo["self"], "_post_inits", None) is None:
            cls_SigInfo["self"]._post_inits = []


        for base in cls.__bases__ + (cls, ):
            init = cls_init if base is cls else base.__init__

            if init is not object.__init__ and init not in initialized_bases:
                cls_SigInfo(child_callable=init)
                initialized_bases.append(init)


                if getattr(base, "_post_init", None) and base._post_init not in cls_SigInfo["self"]._post_inits:
                    cls_SigInfo["self"]._post_inits.append(base._post_init)
        if cls is cls_SigInfo["self"].__class__ and getattr(cls_SigInfo["self"], "_post_inits", None) is not None:
            for post_init in cls_SigInfo["self"]._post_inits:
                cls_SigInfo(child_callable=post_init)

    cls.__init__ = _wrapper
    return cls


from generallibrary.diagram import TreeDiagram


class _ObjInfo_Children:
    def get_attr_names(self):
        """ Get a list of obj's attributes' names.

            :param ObjInfo self: """
        return dir(self.obj)

    def generate_children(self):
        """ Create ObjInfo children under this one.

            :param ObjInfo self: """
        for attr_name in self.get_attr_names():
            ObjInfo(obj=getattr(self.obj, attr_name), parent=self)


@initBases
class ObjInfo(TreeDiagram, _ObjInfo_Children):
    """ Get whether obj is a module, function, class, method, property or variable.
        Note: Static- and unbound self methods are incorrect for nested class definitions. """
    def __init__(self, obj, parent=None):
        self.obj = obj

        self._class = self.obj.__class__
        self._class_name = self._class.__name__
        self._owner = self._get_owner()

    def _get_owner(self):
        """ Get owner of obj or None. """
        # Check if second last qualname is class
        split_qual_name = getattr(self.obj, "__qualname__", "").split(".")
        if len(split_qual_name) > 1:
            return getattr(self.obj, "__globals__", {}).get(split_qual_name[-2])

    def is_module(self):
        """ Get whether obj is a module. """
        return inspect.ismodule(self.obj)

    def is_function(self):
        """ Get whether obj is a function. """
        return inspect.isfunction(self.obj) and not self.is_method()

    def is_class(self):
        """ Get whether obj is a class. """
        return inspect.isclass(self.obj)

    def is_property(self):
        """ Get whether obj is a property of a class. """
        # return hasattr(self.obj, "fget")
        return inspect.isdatadescriptor(self.obj)

    def is_instance(self):
        """ Get whether obj is an instance of it's class. """
        return not hasattr(self.obj, "__name__") and not self.is_property() and not self.is_method()

    def is_method(self):
        """ Get whether obj is a method. """
        if inspect.ismethod(self.obj) or inspect.ismethoddescriptor(self.obj):
            return True

        if not callable(self.obj):  # Unbound cls and static methods aren't "callable"
            return False

        if isinstance(self.obj, MethodWrapperType):
            return True

        if self._owner:
            if ObjInfo(self._owner).is_class():
                return True
            elif hasattr(self._owner, self.obj.__name__):
                return True

        return False

    def subset_is_method_bound(self):
        """ Subset of `is_method`: Get whether a method is bound. """
        assert self.is_method()

        has_self = hasattr(self.obj, "__self__")
        if has_self:
            return True

        if self._owner and self._owner.__dict__.get(self.obj.__name__) == self.obj:
            return False

        if self._owner and not has_self:
            return True

        return False




from generallibrary.functions import SigInfo



































