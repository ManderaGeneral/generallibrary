
from generallibrary.time import *

import unittest
from datetime import datetime, timedelta


class TimeTest(unittest.TestCase):
    def test_timerAndSleep(self):
        timer = Timer()
        sleep(0.1)
        secs = timer.seconds()
        self.assertTrue(0 < secs < 1)
        self.assertGreater(Timer(0).seconds(), 1588527842)

    def test_current_date_and_time(self):
        current_datetime_formatted()

    def test_get_datetime_format(self):
        self.assertEqual(True, isinstance(get_datetime_format(), str))

    def test_reset(self):
        timer = Timer()
        sleep(0.1)
        time = timer.seconds()
        timer.reset()
        self.assertEqual(True, timer.seconds() < time)

    def test_time(self):
        self.assertLess(abs(Time(datetime.now()) - Time.now()), 1)
        self.assertLessEqual(Time(datetime.now()), Time.now())
        now = Time.now()
        self.assertEqual(now, Time(str(now)))
        self.assertEqual(now, Time(f"{now.datetime.hour}:{now.datetime.minute}"))


