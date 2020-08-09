"""
Get and define python versions.
Get Operating System.
Get package info?
"""

from generallibrary.object import initBases

from packaging import version


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
        """Get whether running on Windows or not"""
        return self._system == self._translate["linux"]

    @property
    def linux(self):
        """Get whether running on Linux or not"""
        return self._system == self._translate["windows"]

    @property
    def mac(self):
        """Get whether running on Mac or not"""
        return self._system == self._translate["mac"]

    @property
    def java(self):
        """Get whether running on Java or not"""
        return self._system == self._translate["java"]

    @property
    def os(self):
        """Return name of running operating system"""
        return self._getOSList()[0]

    def _getOSList(self):
        return [name for name, system in self._translate.items() if getattr(self, name)]


class _PythonInfo:
    """Get info regarding running python version."""
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
        """Return first digit of python version."""
        return self._versionInfo.major

    @property
    def pythonMinor(self):
        """Return second digit of python version."""
        return self._versionInfo.minor

    @property
    def pythonMicro(self):
        """Return third digit of python version."""
        return self._versionInfo.micro

    @property
    def pythonReleaseLevel(self):
        """Return release level of python version.
        It's alpha, beta, candidate or final."""
        return self._versionInfo.releaselevel

    @property
    def pythonSerial(self):
        """Return serial number of python version. I think it's only used for non-final release levels."""
        return self._versionInfo.serial

    @property
    def pythonSerialString(self):
        """Return serial number of python version as a string, should be empty if it's 0."""
        return str(self._versionInfo.serial) if self._versionInfo.serial else ""

    @property
    def pythonAlpha(self):
        """Return whether release level is 'alpha' or not."""
        return self.pythonReleaseLevel == "alpha"

    @property
    def pythonBeta(self):
        """Return whether release level is 'beta' or not."""
        return self.pythonReleaseLevel == "beta"

    @property
    def pythonCandidate(self):
        """Return whether release level is 'candidate' or not."""
        return self.pythonReleaseLevel == "candidate"

    @property
    def pythonFinal(self):
        """Return whether release level is 'final' or not."""
        return self.pythonReleaseLevel == "final"

    @property
    def pythonReleaseKeyword(self):
        """Return keyword for release level such as 'a', 'b', 'rc' or '' for final."""
        return self._releaseLevels[self.pythonReleaseLevel]

    @property
    def pythonString(self):
        """Return python version as '3.8.5' or '3.8.5a4' if alpha release 4."""
        return f"{self.pythonMajor}.{self.pythonMinor}.{self.pythonMicro}{self.pythonReleaseKeyword}{self.pythonSerialString}"

    @property
    def pythonVersion(self):
        """Returns a PythonVersion object that can be used to compare directly to an int, float or str."""
        return PythonVersion(self.pythonString)

@initBases
class VerInfo(_OsInfo, _PythonInfo):
    """Inherits and groups all information classes."""

import typing




comparisonOperators = {
    "__eq__": lambda a, b: a == b,
    "__gt__": lambda a, b: a > b,
    # "__ne__": lambda a, b: a != b,
}


def defineComparisonOperators(leftLambda, rightLambda):
    def wrapper(cls):
        for name, func in comparisonOperators.items():
            setattr(cls, name, lambda self, other, func=func: func(leftLambda(self), rightLambda(other)))

        return cls
    return wrapper




@defineComparisonOperators(lambda self: self._version, lambda other: version.parse(str(other)))
class PythonVersion:
    """To easily compare python versions to float or str."""
    def __init__(self, pythonString):
        self._version = version.parse(pythonString)











