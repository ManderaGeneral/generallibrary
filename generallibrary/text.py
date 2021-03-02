

def comma_and_and(*values, period=True):
    """ Return a properly formatted string, eg: a, b and c. """
    period = '.' if period else ''
    len_values = len(values)
    if len_values == 0:
        return ""
    elif len_values == 1:
        return f"{values[0]}{period}"
    else:
        return f"{', '.join(values[:-1])} and {values[-1]}{period}"


def plur_sing(count, word, suffix=None):
    """ Conditionally add an 's' for example, if count isn't 1. """
    if suffix is None:
        suffix = "s"
    return f"{count} {word}{suffix * (count != 1)}"
