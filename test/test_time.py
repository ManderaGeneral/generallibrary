
import unittest

from generallibrary.time import Timer, sleep


class TimeTest(unittest.TestCase):
    def test_timerAndSleep(self):
        timer = Timer()
        sleep(0.1)
        secs = timer.seconds()
        self.assertTrue(0.09 < secs < 0.2)
        self.assertGreater(Timer(0).seconds(), 1588527842)
