
from generallibrary.versions import *

import unittest
import os


class VersionsTest(unittest.TestCase):
    def test_os(self):
        verInfo = VerInfo()
        self.assertTrue(verInfo.os in verInfo._translate)
        self.assertEqual(1, sum((verInfo.windows, verInfo.linux, verInfo.mac, verInfo.java)))

    def test_caseSensitive(self):
        with open("Foo", "w") as file:
            file.write("bar")
        try:
            with open("foo", "r"):
                pass
        except FileNotFoundError:
            sensitive = True
        else:
            sensitive = False
        os.remove("Foo")
        self.assertEqual(sensitive, VerInfo().caseSensitive)

    def test_pathDelimiter(self):
        self.assertIn(VerInfo().pathDelimiter, ("/", "\\"))

    def test_PythonVersion(self):
        verInfo = VerInfo()
        self.assertGreaterEqual(verInfo.pythonMajor, 2)
        self.assertGreaterEqual(verInfo.pythonMinor, 0)
        self.assertGreaterEqual(verInfo.pythonMicro, 0)
        self.assertGreaterEqual(verInfo.pythonSerial, 0)
        self.assertGreaterEqual("", verInfo.pythonSerialString)

        self.assertEqual(1, sum((verInfo.pythonAlpha, verInfo.pythonBeta, verInfo.pythonCandidate, verInfo.pythonFinal)))

        self.assertLessEqual(len(verInfo.pythonReleaseKeyword), 2)
        self.assertLessEqual("final", verInfo.pythonReleaseLevel)

        self.assertLessEqual(verInfo.pythonString.count("."), 2)

        self.assertTrue(verInfo.pythonVersion > 2)
        self.assertTrue(verInfo.pythonVersion > 2.1)
        self.assertTrue(verInfo.pythonVersion > "2.0.1")
        self.assertFalse(verInfo.pythonVersion > verInfo.pythonString)

        self.assertFalse(verInfo.pythonVersion < 2)
        self.assertFalse(verInfo.pythonVersion < 2.1)
        self.assertFalse(verInfo.pythonVersion < "2.0.1")
        self.assertFalse(verInfo.pythonVersion < verInfo.pythonString)

        self.assertTrue(verInfo.pythonVersion >= 2)
        self.assertTrue(verInfo.pythonVersion >= 2.1)
        self.assertTrue(verInfo.pythonVersion >= "2.0.1")
        self.assertTrue(verInfo.pythonVersion >= verInfo.pythonString)

        self.assertFalse(verInfo.pythonVersion <= 2)
        self.assertFalse(verInfo.pythonVersion <= 2.1)
        self.assertFalse(verInfo.pythonVersion <= "2.0.1")
        self.assertTrue(verInfo.pythonVersion <= verInfo.pythonString)

        self.assertFalse(verInfo.pythonVersion == 2)
        self.assertFalse(verInfo.pythonVersion == 2.1)
        self.assertFalse(verInfo.pythonVersion == "2.0.1")
        self.assertTrue(verInfo.pythonVersion == verInfo.pythonString)

    def test_conditionalFunctionalities(self):
        verInfo = VerInfo()
        self.assertEqual(1, sum((verInfo.pathRootHasColon, verInfo.pathRootIsDelimiter)))

    def test_packages(self):
        self.assertEqual(True, len(get_installed_packages()) > 0)
        self.assertEqual(True, package_is_installed("generallibrary"))
        self.assertEqual(True, package_is_installed("generallibrary", "pyperclip"))
        self.assertEqual(False, package_is_installed("generallibrary", "random_package_not_existing"))

    def test_bump(self):
        self.assertEqual("1.0.0", Ver(1.0))
        self.assertEqual("1.0.0", Ver("1.0"))
        self.assertEqual("1.0.0", Ver("1.0.0"))
        self.assertEqual("1.0.1", Ver("1.0").bump())
        self.assertEqual("1.0.1", Ver("1.0.0").bump())
        self.assertEqual("1.2.4", Ver("1.2.3").bump())
        self.assertEqual("1.2.10", Ver("1.2.9").bump())













































