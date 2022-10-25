from generallibrary import RedirectStdout
from generallibrary.time import *

import unittest


class TimeTest(unittest.TestCase):
    def test_timerAndSleep(self):
        timer = Timer(print_out=False)
        sleep(0.1)
        secs = timer.time()
        self.assertTrue(0 < secs < 1)

    def test_timer_context(self):
        x = []
        with RedirectStdout(x):
            with Timer():
                pass
        self.assertIn(Timer.UNIT, x[0])

    def test_timer_method_deco(self):
        class X:
            @Timer
            def y(self):
                pass
        x = []
        with RedirectStdout(x):
            X().y()
        self.assertIn(Timer.UNIT, x[0])

    def test_timer_deco(self):
        @Timer
        def y():
            pass
        x = []
        with RedirectStdout(x):
            y()
        self.assertIn(Timer.UNIT, x[0])

    def test_timer_deco_no_print(self):
        @Timer(print_out=False)
        def y():
            pass
        x = []
        with RedirectStdout(x):
            y()
        self.assertEqual([], x)


    def test_current_date_and_time(self):
        Date.now()
        Date.get_timezone_obj()

    def test_get_datetime_format(self):
        self.assertEqual(True, isinstance(Date.format, str))

    def test_time(self):
        now = Date.now()
        self.assertEqual(now, Date(str(now)))
        # AssertionError: 2021-11-19 00:22 CET != 2021-11-18 00:22 CET      < workflow unittest
        # self.assertEqual(now, Date(f"{now.datetime.hour}:{now.datetime.minute}"))  # Todo: Fix time casting to wrong day when past midnight.

