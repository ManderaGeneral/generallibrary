"""."""
import unittest

from generallibrary.versions import VerInfo


class VersionsTest(unittest.TestCase):
    def test_os(self):
        verInfo = VerInfo()
        self.assertTrue(verInfo.os in verInfo._translate)
        self.assertEqual(1, sum((verInfo.windows, verInfo.linux, verInfo.mac, verInfo.java)))



