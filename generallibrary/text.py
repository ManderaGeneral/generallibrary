
import re



def _comma_and_helper(*values, period, and_or_or):
    period = '.' if period else ''
    len_values = len(values)
    if len_values == 0:
        return ""
    elif len_values == 1:
        return f"{values[0]}{period}"
    else:
        return f"{', '.join(values[:-1])} {and_or_or} {values[-1]}{period}"

def comma_and_and(*values, period=True):
    """ Return a properly formatted string, eg: a, b and c. """
    return _comma_and_helper(*values, period=period, and_or_or="and")

def comma_and_or(*values, period=True):
    """ Return a properly formatted string, eg: a, b or c. """
    return _comma_and_helper(*values, period=period, and_or_or="or")


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


# Had an idea here to create a convention where you can define different name lengths for your class and then use this func to retrieve with fallbacks
# def name(obj, length: Literal["full", None, "short", "abbr"]=None):
#     if length is None:
#         key = "name"
#     else:
#     if hasattr(obj, f"name_length")














