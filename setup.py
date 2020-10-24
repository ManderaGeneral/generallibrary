
from setuptools import setup, find_packages

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="generallibrary",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Rickard "Mandera" Abraham',
    url="https://github.com/ManderaGeneral/generallibrary",
    version="2.1.11",
    description=(
        "Random useful code made by me, categorized into modules to be imported seperately."
    ),
    packages=find_packages(),
    install_requires=["wheel", "packaging"],
    extras_require={
        "full": ["pandas"],
        "md_features": ["pandas"],
    },
    python_requires=">= 3.7, < 3.9",
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
