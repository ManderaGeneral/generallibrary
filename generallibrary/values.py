
from math import ceil


def clamp(value, minimum, maximum):
    """
    Return clamped value between minimum and maximum.
    """
    if maximum < minimum:
        raise ValueError(f"{maximum} is smaller than {minimum}")

    return max(minimum, min(value, maximum))

def confineTo(value, minimum, maximum):
    """
    Confine this value, but unlike clamp it subtracts diff * n to create an 'infinite' effect
    """
    if maximum < minimum:
        raise ValueError(f"{maximum} is smaller than {minimum}")

    if maximum == minimum:
        return maximum

    diff = maximum - minimum
    if value < minimum:
        value += ceil((minimum - value) / diff) * diff
    if value > maximum:
        value -= ceil((value - maximum) / diff) * diff
    return value
