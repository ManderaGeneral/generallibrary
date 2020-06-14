
from math import ceil


def clamp(value, minimum, maximum):
    """
    Return clamped value between minimum and maximum.
    """
    if maximum < minimum:
        raise ValueError(f"{maximum} is smaller than {minimum}")

    return max(minimum, min(value, maximum))

def inrange(value, minimum, maximum):
    """
    Return whether value is between minimum and maximum.
    """
    if maximum < minimum:
        raise ValueError(f"{maximum} is smaller than {minimum}")

    return minimum <= value <= maximum

def rectify(value, threshold):
    """
    Return 0 if it's below threshold, otherwise difference
    """
    if value < threshold:
        return 0
    return value - threshold

def doubleRectify(value, minimum, maximum):
    """
    Return 0 if it's between min and max, otherwise it returns difference from edge of range.
    """
    if maximum < minimum:
        raise ValueError(f"{maximum} is smaller than {minimum}")

    if inrange(value, minimum, maximum):
        return 0

    if value < minimum:
        return value - minimum
    elif value > maximum:
        return value - maximum

def confineTo(value, minimum, maximum, jumpMargin=1):
    """
    Confine this value, but unlike clamp it subtracts diff * n to create an 'infinite' effect.

    :param float value: Value to be confined
    :param float minimum: Minimum value
    :param float maximum: Maximum value
    :param float jumpMargin: A value that is removed for each call (not jump), when jumping.
        If left at 1 then index searching won't skip first or last index for example.
        If jump is less than jumpMargin then the actual jump length is removed instead.
    :return: A confined value
    """
    if maximum < minimum:
        raise ValueError(f"{maximum} is smaller than {minimum}")

    if maximum == minimum:
        return maximum

    return minimum + rectify(value, minimum, maximum) % (maximum - minimum)
