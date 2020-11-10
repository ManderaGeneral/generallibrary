
from setuptools import setup, find_namespace_packages
from os import path
import configparser
import json
from itertools import chain



def remove_duplicates(l):
    """ Remove all duplicates in a list.
        Values must be hashable as they are passed through as dict keys. (Lists work but not Dicts) """
    return list(set(l))

class Cfg:
    """ Convert cfg file to json. """
    def __init__(self, path):
        self.config = configparser.RawConfigParser()
        self.config.read(path)

    def __call__(self, section, option):
        result = self.config.get(section, option)
        try:
            return json.loads(self.config.get(section, option))
        except json.decoder.JSONDecodeError:
            return result

cfg = Cfg("package_specific.cfg")



this_directory = path.abspath(path.dirname(__file__))  # Same here, could probably use generalfile itself
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

extras_require = cfg("setup", "extras_require")
extras_require["full"] = remove_duplicates([package for package in chain(*list(extras_require.values()))])

classifiers=[
    "Operating System :: Microsoft :: Windows :: Windows 7",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "Operating System :: POSIX :: Linux",
    "Operating System :: MacOS",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "License :: OSI Approved :: MIT License",
]
classifiers.extend(cfg("setup", "classifiers"))

install_requires = cfg("setup", "install_requires")

setup(
    author='Rickard "Mandera" Abraham',
    long_description_content_type="text/markdown",
    url=f"https://github.com/ManderaGeneral/{ cfg('setup', 'name') }",
    license="MIT",
    python_requires=">= 3.8, < 3.10",
    packages=find_namespace_packages(),

    name=cfg("setup", "name"),
    version=cfg("setup", "version"),
    description=cfg("setup", "description"),

    install_requires=install_requires,
    extras_require=extras_require,
    long_description=long_description,
    classifiers=classifiers,
)
