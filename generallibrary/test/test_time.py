
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
        Date.now()
        Date.get_timezone_obj()

    def test_get_datetime_format(self):
        self.assertEqual(True, isinstance(Date.format, str))

    def test_reset(self):
        timer = Timer()
        sleep(0.1)
        time = timer.seconds()
        timer.reset()
        self.assertEqual(True, timer.seconds() < time)

    def test_time(self):
        now = Date.now()
        self.assertEqual(now, Date(str(now)))
        self.assertEqual(now, Date(f"{now.datetime.hour}:{now.datetime.minute}"))

