"""."""
import unittest

from generallibrary.versions import VerInfo


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

        # HERE **
