
import unittest

from generallibrary.time import Timer, sleep

class TimeTest(unittest.TestCase):
    def test_timer(self):
        timer = Timer()
        sleep(0.05)
        secs = timer.seconds()
        self.assertEqual(round(secs, 2), 0.05)

    def test_sleep(self):
        pass