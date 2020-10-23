
# import importlib

def debug(scope, *evals, printOut=True):
    """
    Easily call eval() on an arbitrary amount of evaluation strings.
    Useful for debugging.

    Example:
        debug(locals(), "value", "value + jumpValue", printOut=True)
        debug(locals())  # Prints all objects in scope

    :param dict scope: Just write locals()
    :param str evals: Variable names with or without operations
    :param printOut: Whether to print directly or not
    :return: A nicely formatted string
    """
    if not evals:
        evals = list(scope.keys())

    lines = []
    n = max([len(string) for string in evals])
    for evalStr in evals:
        lines.append(f"{evalStr:>{n}} = {eval(evalStr, scope)}")
    lines.append("")
    text = "\n".join(lines)
    if printOut:
        print(text)
    return text

def getLocalFeaturesAsMD(loc, package):
    """ Convert local callable objects that don't start with `_` to a markdown table for a README.
        Could probably improve it by only having module / package name as a parameter.

        Examples:
            print(getLocalFeaturesAsMD({k: getattr(Path, k, None) for k in dir(Path)}, "generalfile"))
            print(getLocalFeaturesAsMD(locals(), "generallibrary"))
            print(getLocalFeaturesAsMD(dict(Vec2.__dict__), "generalvector"))

        Use `copy_function_metadata` in decorators if data is incorrect.
        """
    import pandas as pd  # Should tell user to use `pip install generallibrary[md_features]`

    rows = []

    for key, value in loc.items():
        if key.startswith("_") or not callable(value):
            continue

        docLines = str(value.__doc__).split("\n")
        if not docLines[0] and len(docLines) > 1:
            doc = docLines[1]
        else:
            doc = docLines[0]

        module = getattr(value, "__module__", "")
        if module.startswith(package):
            rows.append({"Module": module.split(".")[1], "Name": key, "Explanation": doc})

    df = pd.DataFrame(rows)

    df.sort_values(inplace=True, by=["Module", "Name"])

    print("## Features")
    print(df.to_markdown(index=False))

# def import_optional_package(package_name):
#     """ Import a package dynamically.
#         Recommended to use with deco_cache on a static class method. """
#     try:
#         return importlib.import_module(package_name)
#     except ModuleNotFoundError:
#         raise ModuleNotFoundError(f"Optional package '{package_name}' isn't installed.")





