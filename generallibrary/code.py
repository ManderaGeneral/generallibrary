



class _Line:
    def __init__(self, indent, code_str, space_before=0, space_after=0):
        self.indent = indent
        self.code_str = code_str
        self.space_before = space_before
        self.space_after = space_after

class CodeGen:
    """ Tool to help with printing code line by line. """
    indent = " " * 4
    def __init__(self):
        self.lines = []

    def add(self, indent, code_str, space_before=0, space_after=0):
        """ Add a new line. """
        self.lines.append(_Line(indent=indent, code_str=code_str, space_before=space_before, space_after=space_after))

    def generate(self):
        lines = ["############### GENERATED CODE ###############"]
        for line in self.lines:
            for _ in range(line.space_before):
                lines.append("")
            lines.append(f"{self.indent * line.indent}{line.code_str}")
            for _ in range(line.space_after):
                lines.append("")
        lines.append("##############################################")
        return lines

    def print(self):
        print("\n".join(self.generate()))

def args_to_attrs(local_dict):
    """ Print code for a dunder init method to store all arguments as attributes. """
    code = CodeGen()
    for key, value in local_dict.items():
        if key != "self":
            code.add(2, f"self.{key} = {key}")
    code.print()





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





