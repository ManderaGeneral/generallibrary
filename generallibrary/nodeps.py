from importlib.util import find_spec

import pkg_resources


def get_installed_packages():
    """ Get a list of all installed packages as strings. """
    return [pkg.key for pkg in pkg_resources.working_set]


def package_is_installed(*names):
    """ Returns whether a package is installed. """
    for name in names:
        if find_spec(name) is None:
            return False
    return True
