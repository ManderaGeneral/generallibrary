
from generallibrary.functions import Operators

import time
from datetime import datetime
import pytz
from dateutil import parser
from dateutil.tz import gettz
import timeit


class Timer:
    """ Callable class to easily time things and print. """
    def __init__(self, start_time=None):
        """ Returns a started Timer instance.

            :param float start_time: Defaults to time in seconds since epoch (time.time()) """
        self.start_time = self.reset(start_time=start_time)

    def reset(self, start_time=None):
        """ Reset and start timer. """
        if start_time is None:
            start_time = time.time()
        self.start_time = start_time
        return start_time

    def seconds(self):
        """ Get seconds passed since timer started or was reset. """
        return time.time() - self.start_time

    def print(self, reset=False):
        """ Print seconds passed. """
        print(f"Seconds passed: {self.seconds()}")
        if reset:
            self.reset()

    @classmethod
    def deco(cls, iterations=1):
        def _deco(func):
            def _wrapper(*args, **kwargs):
                timer = timeit.default_timer()
                for _ in range(iterations):
                    result = func(*args, **kwargs)
                print(f"Seconds for {iterations} iterations of '{func.__name__}': {timeit.default_timer() - timer}")
                return result
            return _wrapper
        return _deco


def sleep(seconds):
    """ Normal sleep function from time package.

        :param float seconds: Time in seconds to sleep. """
    time.sleep(seconds)


@Operators.deco_define_comparisons(lambda date: date.datetime)
class Date:
    """ Simplify datetime, truncating seconds and microseonds for now. """
    timezone = "Europe/Paris"
    format = "%Y-%m-%d %H:%M %Z"

    def __init__(self, date):
        if isinstance(date, Date):
            datetime = date.datetime
        else:
            if isinstance(date, str):
                datetime = parser.parse(date, tzinfos={"CET": gettz("CET"), "CEST": gettz("CEST")})
            else:
                datetime = date

            if str(datetime.tzinfo) != self.timezone:
                datetime = self.get_timezone_obj().localize(datetime.replace(tzinfo=None))

            datetime = datetime.replace(second=0, microsecond=0)

        self.datetime = datetime

    @classmethod
    def get_timezone_obj(cls):
        return pytz.timezone(cls.timezone)

    @classmethod
    def now(cls):
        return Date(datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(cls.get_timezone_obj()))

    def __sub__(self, other):
        difference = self.datetime - Date(other).datetime
        return difference.total_seconds()

    def __str__(self):
        return self.datetime.strftime(self.format)

    def __repr__(self):
        return str(self)
        # return repr(self.datetime)












































