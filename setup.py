from setuptools import setup

setup(
    name = "generallibrary",
    version = "1.2.2",
    description = (""
                   "Added 'base' folders inside packages 'test' and 'generallibrary'."
                   " This extra step of folders stops importing from importing the files directly, and only being imported through the __init__ file."
                   " Random functions to help with native classes."
                   ""),
    packages = ["generallibrary"]
)


