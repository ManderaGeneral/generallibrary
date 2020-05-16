from setuptools import setup, find_packages

setup(
    name = "generallibrary",
    version = "1.7.5",
    description = (""
                   "Changed iterable() to getIterable()."
                   " Random functions to help with native classes."
                   ""),
    packages = find_packages(),
    install_requires = ['wheel']
)


