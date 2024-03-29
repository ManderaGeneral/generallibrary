
from setuptools import setup, find_namespace_packages
from pathlib import Path

try:
    long_description = (Path(__file__).parent / 'README.md').read_text(encoding='utf-8')
except FileNotFoundError:
    long_description = 'Readme missing'

setup(
    name="generallibrary",
    author='Rickard "Mandera" Abraham',
    author_email="rickard.abraham@gmail.com",
    version="2.10.0",
    description="Random useful code categorized into modules.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'generalimport',
        'generaltool',
        'packaging',
        'pyperclip',
        'pytz',
        'dill',
    ],
    url="https://github.com/ManderaGeneral/generallibrary",
    license="apache2",
    packages=find_namespace_packages(exclude=("build*", "dist*")),
    extras_require={
        'table': ['pandas', 'tabulate'],
        'graph': ['matplotlib', 'networkx'],
        'full': ['matplotlib', 'networkx', 'pandas', 'tabulate'],
    },
    classifiers=[
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
    ],
)
