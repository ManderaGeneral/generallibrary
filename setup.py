from setuptools import setup, find_packages

setup(
    name = "generallibrary",
    version = "1.7.0",
    description = (""
                   "Added None support and changed bool to not be int."
                   " Random functions to help with native classes."
                   ""),
    packages = find_packages(),
    install_requires = ['wheel']
)


