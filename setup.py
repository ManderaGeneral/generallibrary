
from setuptools import setup, find_packages
from os import path
from itertools import chain
from generallibrary import remove_duplicates


extras_require = {
    "md_features": ["pandas"],
}

extras_require["full"] = remove_duplicates([package for package in chain(*list(extras_require.values()))])

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="generallibrary",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Rickard "Mandera" Abraham',
    url="https://github.com/ManderaGeneral/generallibrary",
    version="2.2.0",
    description=(
        "Random useful code categorized into modules."
    ),
    packages=find_packages(),
    install_requires=["wheel", "packaging"],
    extras_require=extras_require,
    python_requires=">= 3.7, < 3.9",
    license="MIT",
    classifiers=[
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",

        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
