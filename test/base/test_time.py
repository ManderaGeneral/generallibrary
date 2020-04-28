
from base.time import *
import unittest


class TimeTest(unittest.TestCase):
    def test_timer(self):
        timer = Timer()
        time.sleep(0.05)
        secs = timer.seconds()
        self.assertEqual(round(secs, 2), 0.05)

    def test_sleep(self):
        pass