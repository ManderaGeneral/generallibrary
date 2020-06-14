
import unittest

from generallibrary.values import clamp, inrange, rectify, doubleRectify, confineTo


class ValuesTest(unittest.TestCase):
    def test_clamp(self):
        self.assertEqual(5, clamp(2, 5, 10))
        self.assertEqual(7, clamp(7, 5, 10))
        self.assertEqual(10, clamp(10.1, 5, 10))
        self.assertEqual(10.2, clamp(20, 5, 10.2))
        self.assertEqual(-3, clamp(-5, -3, 10.2))
        self.assertEqual(-1.4, clamp(-1.4, -3, 10.2))

    def test_inrange(self):
        self.assertEqual(True, inrange(1, 0, 2))
        self.assertEqual(True, inrange(1, 1, 1))
        self.assertEqual(True, inrange(1, 1.0, 1))
        self.assertEqual(True, inrange(0.55, 0.5, 0.6))

        self.assertEqual(False, inrange(0, 1, 1))
        self.assertEqual(False, inrange(2, 1, 1))

        self.assertEqual(True, inrange(-3, -4, -2))
        self.assertEqual(False, inrange(3, -4, -2))

    def test_rectify(self):
        self.assertEqual(2, rectify(2, 0))
        self.assertEqual(1, rectify(2, 1))
        self.assertEqual(3, rectify(2, -1))
        self.assertEqual(0, rectify(2, 3))
        self.assertEqual(0, rectify(2, 2))
        self.assertAlmostEqual(0.1, rectify(2.1, 2))

    def test_doubleRectify(self):
        # HERE ** Add doubleRectify to confineTo later
        self.assertEqual(0, doubleRectify(3, 2, 4))

    def test_confineTo(self):
        self.assertEqual(7, confineTo(2, 5, 10))
        self.assertEqual(7, confineTo(7, 5, 10))
        self.assertEqual(5.1, confineTo(10.1, 5, 10))
        self.assertAlmostEqual(9.6, confineTo(20, 5, 10.2))  # Floating point accuracy problem
        self.assertEqual(8.2, confineTo(-5, -3, 10.2))
        self.assertEqual(-1.4, confineTo(-1.4, -3, 10.2))

        self.assertEqual(3, confineTo(-1.4, 3, 3))

        self.assertEqual(3, confineTo(2, 0, 1))


