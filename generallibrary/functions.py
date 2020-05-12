
import inspect

def leadingArgsCount(func):
    count = 0
    for _, value in inspect.signature(func).parameters.items():
        if value.default is inspect.Parameter.empty:
            count += 1
        else:
            break
    return count

