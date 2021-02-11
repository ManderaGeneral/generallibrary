
from generallibrary.time import *

import unittest


class TimeTest(unittest.TestCase):
    def test_timerAndSleep(self):
        timer = Timer()
        sleep(0.1)
        secs = timer.seconds()
        self.assertTrue(0 < secs < 1)
        self.assertGreater(Timer(0).seconds(), 1588527842)

    def test_current_date_and_time(self):
        current_datetime_formatted()
