"""
Get and define python versions.
Get Operating System.
Get package info?
"""

from generalobjexp import ObjExp

from packaging import version


class Ver:
    def __init__(self):
        import sys
        import platform

        os = {"windows": "Windows", "linux": "Linux", "mac": "Darwin", "java": "Java"}
        self.windows = platform.system() == os["windows"]
        self.linux = platform.system() == os["linux"]
        self.mac = platform.system() == os["mac"]
        self.java = platform.system() == os["java"]

        if sum([getattr(self, name) for name, system in os.items()]) != 1:
            raise AttributeError("OS couldn't be determined")

        self.os = [name for name, system in os.items() if getattr(self, name)][0]

        self.pythonMajor = sys.version_info.major
        self.pythonMinor = sys.version_info.minor
        self.pythonMicro = sys.version_info.micro
        self.python = f"{self.pythonMajor}.{self.pythonMinor}.{self.pythonMicro}"



# from pip._internal.utils.misc import get_installed_distributions
# ObjExp(get_installed_distributions(), showDunders=True)



# HERE ** Experimenting with getting package versions
import sys
for name, module in sorted(sys.modules.items()):
    if hasattr(module, '__version__'):
        print(name, module.__version__ )

ver = Ver()

# print(ObjExp.__module__)

print(version.parse(ver.python) > version.parse("3.7.5"))






