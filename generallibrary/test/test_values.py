
from generallibrary.values import *

import unittest


class ValuesTest(unittest.TestCase):
    def test_floor(self):
        self.assertEqual(5, floor(5.7))
        self.assertEqual(5, floor(5.1))
        self.assertEqual(5, floor(5))
        self.assertEqual(5, floor(5.5, 0))

        self.assertEqual(50, floor(54.2, -1))
        self.assertEqual(0, floor(54.2, -2))
        self.assertEqual(0, floor(54.2, -5))

        self.assertEqual(0, floor(154.2512, -3))
        self.assertEqual(100, floor(154.2512, -2))
        self.assertEqual(150, floor(154.2512, -1))
        self.assertEqual(154, floor(154.2512, 0))
        self.assertEqual(154.2, floor(154.2512, 1))
        self.assertEqual(154.25, floor(154.2512, 2))
        self.assertEqual(154.251, floor(154.2512, 3))
        self.assertEqual(154.2512, floor(154.2512, 4))
        self.assertEqual(154.2512, floor(154.2512, 5))

    def test_ceil(self):
        self.assertEqual(6, ceil(5.7))
        self.assertEqual(6, ceil(5.1))
        self.assertEqual(5, ceil(5))
        self.assertEqual(6, ceil(5.5, 0))

        self.assertEqual(60, ceil(54.2, -1))
        self.assertEqual(100, ceil(54.2, -2))
        self.assertEqual(1000, ceil(54.2, -3))

        self.assertEqual(1000, ceil(154.2512, -3))
        self.assertEqual(200, ceil(154.2512, -2))
        self.assertEqual(160, ceil(154.2512, -1))
        self.assertEqual(155, ceil(154.2512, 0))
        self.assertEqual(154.3, ceil(154.2512, 1))
        self.assertEqual(154.26, ceil(154.2512, 2))
        self.assertEqual(154.252, ceil(154.2512, 3))
        self.assertEqual(154.2512, ceil(154.2512, 4))

    def test_clamp(self):
        self.assertEqual(5, clamp(2, 5, 10))
        self.assertEqual(7, clamp(7, 5, 10))
        self.assertEqual(10, clamp(10.1, 5, 10))
        self.assertEqual(10.2, clamp(20, 5, 10.2))
        self.assertEqual(-3, clamp(-5, -3, 10.2))
        self.assertEqual(-1.4, clamp(-1.4, -3, 10.2))

    def test_sign(self):
        self.assertEqual(-1, sign(-5))
        self.assertEqual(-1, sign(-0.1))

        self.assertEqual(0, sign(-0))
        self.assertEqual(0, sign(0))

        self.assertEqual(1, sign(0.1))
        self.assertEqual(1, sign(3))

        self.assertEqual(1, sign(-2, -3))
        self.assertEqual(0, sign(-2, -2))
        self.assertEqual(-1, sign(-2, -1))

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
        self.assertEqual(0, doubleRectify(3, 2, 4))
        self.assertEqual(-1, doubleRectify(1, 2, 4))
        self.assertEqual(1, doubleRectify(5, 2, 4))
        self.assertAlmostEqual(0.1, doubleRectify(4.1, 2, 4))
        self.assertEqual(-3.5, doubleRectify(-1.5, 2, 4))

    def test_confineTo(self):
        self.assertEqual(7, confineTo(2, 5, 10))
        self.assertEqual(7, confineTo(7, 5, 10))
        self.assertEqual(5.1, confineTo(10.1, 5, 10))
        self.assertAlmostEqual(9.6, confineTo(20, 5, 10.2))  # Floating point accuracy problem
        self.assertEqual(8.2, confineTo(-5, -3, 10.2))
        self.assertEqual(-1.4, confineTo(-1.4, -3, 10.2))

        self.assertEqual(3, confineTo(-1.4, 3, 3))

        self.assertEqual(0.5, confineTo(1.5, 0, 1))
        self.assertEqual(1, confineTo(2, 0, 1))

        self.assertEqual(0, confineTo(2, 0, 1, margin=0.5))
        self.assertEqual(1, confineTo(-1, 0, 1, margin=0.5))
        self.assertEqual(0, confineTo(-2, 0, 1, margin=0.5))
        self.assertEqual(1, confineTo(-3, 0, 1, margin=0.5))

        self.assertEqual(1.4, confineTo(1.4, 0, 1, margin=0.5))
        self.assertEqual(1.5, confineTo(1.5, 0, 1, margin=0.5))
        self.assertEqual(-0.49, confineTo(1.51, 0, 1, margin=0.5))

    def test_EnvVar(self):
        envVar = EnvVar("testing")
        with self.assertRaises(KeyError):
            x = envVar.value
        envVar.value = "foo"
        self.assertEqual("foo", envVar.value)

    def test_get_launch_options(self):
        launch_options = get_launch_options()
        self.assertEqual(True, not launch_options or launch_options[0] == "discover")























