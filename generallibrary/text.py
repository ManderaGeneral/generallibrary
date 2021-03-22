
import re


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


def _pattern(pattern):
    return re.escape(str(pattern))


def replace(string, reverse=False, **translation):
    """ Replace strings in a string with other strings!
        Uses regex and * is treated as wildcard. """
    for a, b in translation.items():
        if reverse:
            a, b = b, a
        string = re.sub(_pattern(a), str(b).replace("\\", "\\\\"), string)
    return string


def match(string, *patterns):
    """ Search string for matches, True if any match is found.
        Uses regex and * is treated as wildcard. """
    return any(re.search(replace(_pattern(pattern), **{r"\*": ".+"}), string, re.IGNORECASE) for pattern in patterns)

