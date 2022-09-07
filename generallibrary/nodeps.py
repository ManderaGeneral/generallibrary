import importlib
import sys
import pkg_resources

skip_base_classes = []

try:
    from unittest.case import SkipTest
    skip_base_classes.append(SkipTest)
except ImportError:
    pass

try:
    from _pytest.outcomes import Skipped
    skip_base_classes.append(Skipped)
except ImportError:
    pass



def get_installed_packages():
    """ Get a set of all installed packages as strings. """
    return {pkg.key for pkg in pkg_resources.working_set}


def package_is_installed(*names):
    """ Returns whether a package is installed.
        `find_spec(name) is None` was the previous solution but namespaces returned True. """
    packages = get_installed_packages()
    for name in names:
        if name not in packages:
            return False
    return True

def import_module(name, error=True):
    try:
        module = importlib.import_module(name=name)
    except (ModuleNotFoundError, TypeError) as e:
        if error:
            raise e
    else:
        if getattr(module, "__file__", None):  # Got a namespace module without __file__ so filter those out here
            return module

class MissingOptionalDependency(*skip_base_classes):
    def __init__(self, msg=None):
        self.msg = msg

    def __repr__(self):
        if self.msg:
            return f"MissingOptionalDependency: {self.msg}"
        else:
            return f"MissingOptionalDependency"

    def __str__(self):
        return self.msg or "MissingOptionalDependency"


class FakeModule:
    def __init__(self, name):
        self.name = name

    def error_func(self, *args, **kwargs):
        raise MissingOptionalDependency(f"Optional dependency '{self.name}' isn't installed.")

    def __getattr__(self, item):
        return self.error_func

# def extras_require():
#     result = run_setup("./setup.py", stop_after="init")
#     return getattr(result, "extras_require", None)

def optional_packages(*names):
    """ Creates fake packages if they don't exist.
        These fake packages' attrs are always a function that raises a ModuleNotFoundError when called.
        This lets you write minimal code for optional dependencies. """
    # if not names:
    #     names = set(chain(*extras_require().values()))
    #     print(names)

    for name in names:
        if not package_is_installed(name):
            sys.modules[name] = FakeModule(name=name)

