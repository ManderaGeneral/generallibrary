from setuptools import setup, find_packages

setup(
    name = "generallibrary",
    version = "1.7.4",
    description = (""
                   "Replace iterable() with isIterable() in getRows()."
                   " Random functions to help with native classes."
                   ""),
    packages = find_packages(),
    install_requires = ['wheel']
)


