
import unittest

from generallibrary.values import clamp, confineTo


class ValuesTest(unittest.TestCase):
    def test_clamp(self):
        self.assertEqual(5, clamp(2, 5, 10))
        self.assertEqual(7, clamp(7, 5, 10))
        self.assertEqual(10, clamp(10.1, 5, 10))
        self.assertEqual(10.2, clamp(20, 5, 10.2))
        self.assertEqual(-3, clamp(-5, -3, 10.2))
        self.assertEqual(-1.4, clamp(-1.4, -3, 10.2))

    def test_confineTo(self):
        self.assertEqual(7, confineTo(2, 5, 10))
        self.assertEqual(7, confineTo(7, 5, 10))
        self.assertEqual(5.1, confineTo(10.1, 5, 10))
        self.assertAlmostEqual(9.6, confineTo(20, 5, 10.2))  # Floating point accuracy problem
        self.assertEqual(8.2, confineTo(-5, -3, 10.2))
        self.assertEqual(-1.4, confineTo(-1.4, -3, 10.2))

        self.assertEqual(3, confineTo(-1.4, 3, 3))

