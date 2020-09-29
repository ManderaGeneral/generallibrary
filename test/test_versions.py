"""."""
import unittest

from generallibrary.versions import VerInfo, get_installed_packages, package_is_installed


class VersionsTest(unittest.TestCase):
    def test_os(self):
        verInfo = VerInfo()
        self.assertTrue(verInfo.os in verInfo._translate)
        self.assertEqual(1, sum((verInfo.windows, verInfo.linux, verInfo.mac, verInfo.java)))

    def test_python(self):
        verInfo = VerInfo()
        self.assertGreaterEqual(verInfo.pythonMajor, 2)
        self.assertGreaterEqual(verInfo.pythonMinor, 0)
        self.assertGreaterEqual(verInfo.pythonMicro, 0)
        self.assertGreaterEqual(verInfo.pythonSerial, 0)

        self.assertEqual(1, sum((verInfo.pythonAlpha, verInfo.pythonBeta, verInfo.pythonCandidate, verInfo.pythonFinal)))

        self.assertLessEqual(len(verInfo.pythonReleaseKeyword), 2)

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
        self.assertEqual(False, package_is_installed("random_package_not_existing"))















































