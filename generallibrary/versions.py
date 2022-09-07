"""
Get and define python versions.
Get Operating System.
Get package info?
"""

from generallibrary.functions import initBases
from generallibrary.decorators import Operators

from packaging import version
from distutils.version import StrictVersion
import re


class Ver(StrictVersion):
    """ Generic version handler.
        Todo: Use Ver in each part of VerInfo. """
    def __init__(self, ver):
        ver = self._allow_single_digit(ver)
        super().__init__(str(ver))

    @staticmethod
    def _allow_single_digit(ver):
        if isinstance(ver, int) or (isinstance(ver, str) and "." not in ver):
            return float(ver)
        else:
            return ver

    def bump(self):
        """ Return a new Ver with bumped last value. """
        if str(self).count(".") == 0:
            return f"{self}.0.1"
        elif str(self).count(".") == 1:
            return f"{self}.1"
        else:
            bulk, micro = re.findall("(.*)(\\d)", str(self))[0]
            return Ver(f"{bulk}{int(micro) + 1}")

    def __dumps__(self):
        return str(self)

    @staticmethod
    def __loads__(ver):
        return Ver(ver=ver)


class _OsInfo:
    """Get info regarding running operating system."""
    _translate = {
        "windows": "Windows",
        "linux": "Linux",
        "mac": "Darwin",
        "java": "Java"
    }

    def __init__(self):
        import platform

        self._system = platform.system()
        assert len(self._getOSList()) == 1

    @property
    def windows(self):
        """ Get whether running on Windows. """
        return self._system == self._translate["windows"]

    @property
    def linux(self):
        """ Get whether running on Linux. """
        return self._system == self._translate["linux"]

    @property
    def mac(self):
        """ Get whether running on Mac. """
        return self._system == self._translate["mac"]

    @property
    def java(self):
        """ Get whether running on Java. """
        return self._system == self._translate["java"]

    @property
    def os(self):
        """ Return name of running operating system. """
        return self._getOSList()[0]

    def _getOSList(self):
        return [name for name, system in self._translate.items() if getattr(self, name)]


class _PythonInfo:
    """ Get info regarding running python version. """
    _releaseLevels = {
        "alpha": "a",
        "beta": "b",
        "candidate": "rc",
        "final": ""
    }

    def __init__(self):
        import sys
        self._versionInfo = sys.version_info

        assert self.pythonReleaseLevel in self._releaseLevels  # Recognize release level
        assert not (self.pythonFinal and self.pythonSerial)  # Don't think final releases can have a serial number

    @property
    def pythonMajor(self):
        """ Return first digit of python version. """
        return self._versionInfo.major

    @property
    def pythonMinor(self):
        """ Return second digit of python version. """
        return self._versionInfo.minor

    @property
    def pythonMicro(self):
        """ Return third digit of python version. """
        return self._versionInfo.micro

    @property
    def pythonReleaseLevel(self):
        """ Return release level of python version.
            It's alpha, beta, candidate or final. """
        return self._versionInfo.releaselevel

    @property
    def pythonSerial(self):
        """ Return serial number of python version. I think it's only used for non-final release levels. """
        return self._versionInfo.serial

    @property
    def pythonSerialString(self):
        """ Return serial number of python version as a string, should be empty if it's 0. """
        return str(self._versionInfo.serial) if self._versionInfo.serial else ""

    @property
    def pythonAlpha(self):
        """ Return whether release level is 'alpha'. """
        return self.pythonReleaseLevel == "alpha"

    @property
    def pythonBeta(self):
        """ Return whether release level is 'beta'. """
        return self.pythonReleaseLevel == "beta"

    @property
    def pythonCandidate(self):
        """ Return whether release level is 'candidate'. """
        return self.pythonReleaseLevel == "candidate"

    @property
    def pythonFinal(self):
        """ Return whether release level is 'final'. """
        return self.pythonReleaseLevel == "final"

    @property
    def pythonReleaseKeyword(self):
        """ Return keyword for release level such as 'a', 'b', 'rc' or '' for final. """
        return self._releaseLevels[self.pythonReleaseLevel]

    @property
    def pythonString(self):
        """ Return python version as '3.8.5' or '3.8.5a4' if alpha release 4. """
        return f"{self.pythonMajor}.{self.pythonMinor}.{self.pythonMicro}{self.pythonReleaseKeyword}{self.pythonSerialString}"

    @property
    def pythonVersion(self):
        """ Returns a PythonVersion object that can be used to compare directly to an int, float or str. """
        return PythonVersion(self.pythonString)


class _ConditionalFunctionalities:
    """ Groups all functionality properties. """
    @property
    def caseSensitive(self):
        """ Get whether current OS is case sensitive.

            :param VerInfo self: """
        return not self.windows

    @property
    def positionalArgument(self):
        """ Get whether current python version supports positional arguments.

            :param VerInfo self: """
        return self.pythonVersion >= 3.8

    @property
    def pathDelimiter(self):
        """ Get current OS's path delimiter.

            :param VerInfo self: """
        return "\\" if self.windows else "/"

    @property
    def pathRootIsDelimiter(self):
        """ Get whether current OS defines path root as a starting delimiter.

            :param VerInfo self: """
        return not self.windows

    @property
    def pathRootHasColon(self):
        """ Get whether current OS defines path root with a colon in the first part.

            :param VerInfo self: """
        return self.windows


@initBases
class VerInfo(_OsInfo, _PythonInfo, _ConditionalFunctionalities):
    """ Get version info regarding current Python, OS and conditional functionalities.
        Use conditional feature properties if possible. """


class DuckTyping:
    """ I have an idea here to pair syntax tests to python versions.
        We can then run them all and make sure they succeed / fail based on running versions.
        Would have to deal with syntax error by some importing technique then I guess. """


@Operators.deco_define_comparisons(lambda left: left.version, lambda right: version.parse(str(right)))
class PythonVersion(DuckTyping):
    """ Used by VerInfo.pythonVersion to easily compare python versions to int, float or string. """
    def __init__(self, pythonString):
        self._version = version.parse(pythonString)

    @property
    def version(self):
        """ Get python version.
            Protect variable."""
        return self._version


