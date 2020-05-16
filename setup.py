from setuptools import setup, find_packages

setup(
    name = "generallibrary",
    version = "1.7.3",
    description = (""
                   "Added getRows() which we extracted from fileTSV."
                   " Random functions to help with native classes."
                   ""),
    packages = find_packages(),
    install_requires = ['wheel']
)


