
from math import ceil
import os
import sys


def clamp(value, minimum, maximum):
    """
    Return clamped value between minimum and maximum.

    :param float value:
    :param float minimum:
    :param float maximum:
    """
    if maximum < minimum:
        raise ValueError(f"{maximum} is smaller than {minimum}")

    return max(minimum, min(value, maximum))

def sign(value, threshold=0):
    """
    Get sign value based on threshold that defaults to 0.

    :param float value:
    :param float threshold:
    :return: -1, 0 or 1
    """
    if value < threshold:
        return -1

    if value == threshold:
        return 0

    return 1

def inrange(value, minimum, maximum):
    """
    Return whether value is between minimum and maximum.

    :param float value:
    :param float minimum:
    :param float maximum:
    """
    if maximum < minimum:
        raise ValueError(f"{maximum} is smaller than {minimum}")

    return minimum <= value <= maximum

def rectify(value, threshold):
    """
    Return 0 if it's below threshold, otherwise difference.

    :param float value:
    :param float threshold:
    """
    if value < threshold:
        return 0
    return value - threshold

def doubleRectify(value, minimum, maximum):
    """
    Return 0 if it's between min and max, otherwise it returns difference from edge of range.

    :param float value:
    :param float minimum:
    :param float maximum:
    """
    if maximum < minimum:
        raise ValueError(f"{maximum} is smaller than {minimum}")

    if inrange(value, minimum, maximum):
        return 0

    if value < minimum:
        return value - minimum
    elif value > maximum:
        return value - maximum

def confineTo(value, minimum, maximum, margin=0):
    """
    Confine this value, but unlike clamp it subtracts diff * n to create an 'infinite' effect.

    :param float value: Value to be confined
    :param float minimum: Minimum value
    :param float maximum: Maximum value
    :param float margin: A value that represents how far outside min/max value can be before jumping.
        A margin of 0.5 allows integer index searching to not skip any index for example.
    :return: A confined value
    """
    if maximum < minimum:
        raise ValueError(f"{maximum} is smaller than {minimum}")

    if maximum == minimum:
        return maximum

    if inrange(value, minimum, maximum):
        return value

    valueRange = maximum - minimum + margin * 2
    rectifiedValue = doubleRectify(value, minimum - margin, maximum + margin)
    jumps = ceil(abs(rectifiedValue) / valueRange)
    signValue = sign(rectifiedValue) * -1
    jumpValue = jumps * valueRange * signValue

    return value + jumpValue


class EnvVar:
    """ Handles environment variables.
        actions_name has to be defined if the env var is used for unittesting in the workflow. """
    def __init__(self, name, actions_name=None):

        if actions_name is not None:
            actions_name = "${{ " + actions_name + " }}"

        self.name = name
        self.actions_name = actions_name

    @property
    def value(self):
        """ Get value of env var. """
        if self.name not in os.environ:
            raise KeyError(f"Env var '{self.name}' is not set.")

        return os.environ[self.name]

    @value.setter
    def value(self, value):
        """ Set value of an env var, both in instance and os.environ. """
        os.environ[self.name] = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"<{type(self).__name__}: {self.name}>"


def get_launch_options():
    """ Return a dict of given args from launch options.
        Uses sys.argv, attempts to split on '=', if missing then getFreeIndex is used as key.
        WARNING: Removes all extra values in sys.argv (As unittest couldn't handle it) """
    args = {}
    while len(sys.argv) > 1:
        arg = sys.argv[1]
        if "=" in arg:
            split = arg.split("=")
            args[split[0]] = split[1]
        else:
            args[getFreeIndex(args)] = arg
        del sys.argv[1]
    return args


from generallibrary.iterables import getFreeIndex































