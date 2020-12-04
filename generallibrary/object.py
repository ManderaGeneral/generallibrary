
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

    Also looks for defined `__init_post__` methods, stores them in `instance.__init_post__s` and calls them all after all inits.
    """
    cls_init = cls.__init__  # Unbound original __init__ method of class

    cls._is_wrapped_by_initBases = cls

    def _wrapper(*args, **kwargs):
        cls_SigInfo = SigInfo(cls_init, *args, **kwargs)

        if not cls_SigInfo["self"]:
            raise AttributeError(f"{cls} hasn't defined it's `__init__`")

        initialized_bases = []

        if getattr(cls_SigInfo["self"], "__init_post__s", None) is None:
            cls_SigInfo["self"].__init_post__s = []


        for base in cls.__bases__ + (cls, ):
            init = cls_init if base is cls else base.__init__

            if init is not object.__init__ and init not in initialized_bases:
                cls_SigInfo(child_callable=init)
                initialized_bases.append(init)


                if getattr(base, "__init_post__", None) and base.__init_post__ not in cls_SigInfo["self"].__init_post__s:
                    cls_SigInfo["self"].__init_post__s.append(base.__init_post__)
        if cls is cls_SigInfo["self"].__class__ and getattr(cls_SigInfo["self"], "__init_post__s", None) is not None:
            for post_init in cls_SigInfo["self"].__init_post__s:
                cls_SigInfo(child_callable=post_init)

    cls.__init__ = _wrapper
    return cls


from generallibrary.diagram import TreeDiagram


class _children_properties:
    def protected(self):
        """ Get whether possible key is protected, False if key is None.
            Primarily checks __qualname__, falls back on `self.get_key()`.

            :param ObjInfo self: """
        if self._split_qual_name:
            return self._split_qual_name[-1].startswith("_")
        else:
            return str(self.get_key()).startswith("_")


class _children_origins:
    def from_instance(self):
        """ Get whether this attribute came from the instance.

            :param ObjInfo self: """
        if parent := self.generate_parent():
            return getattr(parent.obj, str(self.get_key()), object()) != self.obj
        else:
            return False



class _ObjInfo_children(_children_properties, _children_origins):
    def get_attribute_child(self, key):
        """ Create a single ObjInfo from this instance's attribute key and put as child.

            :param ObjInfo self:
            :param key: Attribute key. """
        return ObjInfo(obj=getattr(self.obj, key), parent=self)

    def generate_attributes(self, protected=False, **methods):
        """ Generate ObjInfo attribute children with filters correlating to ObjInfo's methods.

            :param ObjInfo self:
            :param protected: """
        methods.update({key: value for key, value in locals().items() if key not in ("self", "methods")})

        for key in dir(self.obj):
            objInfo = self.get_attribute_child(key)
            for method_name, boolean in methods.items():
                if getattr(objInfo, method_name)() != boolean:
                    objInfo.remove()
                    break
        return self


class _ObjInfo_type:
    def is_module(self):
        """ Get whether obj is a module.

            :param ObjInfo self: """
        return inspect.ismodule(self.obj)

    def is_function(self):
        """ Get whether obj is a function.

            :param ObjInfo self: """
        return inspect.isfunction(self.obj) and not self.is_method()

    def is_class(self):
        """ Get whether obj is a class.

            :param ObjInfo self: """
        return inspect.isclass(self.obj)

    def is_property(self):
        """ Get whether obj is a property of a class.

                :param ObjInfo self: """
        # return hasattr(self.obj, "fget")
        return inspect.isdatadescriptor(self.obj)

    def is_instance(self):
        """ Get whether obj is an instance of it's class.

            :param ObjInfo self: """
        return not hasattr(self.obj, "__name__") and not self.is_property() and not self.is_method()

    def is_method(self):
        """ Get whether obj is a method.

            :param ObjInfo self: """
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


# HERE **
# Add methods to retrieve origin and add new feature to get attributes defined by a certain class
# Then we can change test to get all _ObjInfo_type's methods instead of is_*
# Then we can change protected to is_protected etc


@initBases
class ObjInfo(TreeDiagram, _ObjInfo_children, _ObjInfo_type):
    """ Get whether obj is a module, function, class, method, property or variable.
        Automatically generates parents with `get_parent` when needed.
        Children are generated with `generate_attributes`.
        Nested definitions are not att"""
    def __init__(self, obj, parent=None, key=None):
        self.obj = obj
        self.key = getattr(self.obj, "__name__", key)

        if self.key is None:
            raise AttributeError(f"Could not set key for {self.obj}, must be set manually.")

    def get_parent(self, index=0):
        """ Tries to generate parent with dunder- qualname and globals if index is 0.

            :param ObjInfo self:
            :param index:

            Todo: Handle <locals> in qualname. """
        if parent := super().get_parent(index=index):
            return parent

        elif index == 0:
            module_name = getattr(self.obj, "__module__", None)
            module = sys.modules.get(module_name)

            split_qualname = qualname.split(".") if (qualname := getattr(self.obj, "__qualname__", None)) else []

            if len(split_qualname) > 1:

                if obj_globals := getattr(self.obj, "__globals__", None):

                for i, name in enumerate(split_qualname[-2::-1]):
                    if parent_obj := obj_globals.get(name):
                        for i2 in range(i):
                            parent_obj = getattr(parent_obj, split_qualname[-2 - i + i2 + 1])
                        return self.set_parent(parent=ObjInfo(parent_obj), old_parent=None)

            elif module:
                return self.set_parent(parent=ObjInfo(module), old_parent=None)

    def hook_new_parent(self, parent, old_parent):
        """ Assert that child's key is in parent's dir.
            If key is None then we search for child in dir. """
        assert self.key in dir(parent.obj)


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


































