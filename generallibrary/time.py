
from generallibrary.functions import Operators

import time
from datetime import datetime
import pytz
from dateutil import parser
from dateutil.tz import gettz


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


def sleep(seconds):
    """ Normal sleep function from time package.

        :param float seconds: Time in seconds to sleep. """
    time.sleep(seconds)


# HERE ** Remove old funcs
def current_datetime(timezone=None):
    """ Get current aware datetime. """
    if timezone is None:
        timezone = "Europe/Paris"
    return datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(pytz.timezone(timezone))


def get_datetime_format():
    return "%Y-%m-%d %H:%M %Z"


def current_datetime_formatted(timezone=None, format_str=None):
    """ Get a nicely formatted date and time string. """
    if timezone is None:
        timezone = "Europe/Paris"
    if format_str is None:
        format_str = get_datetime_format()
    return current_datetime(timezone=timezone).strftime(format_str)


@Operators.deco_define_comparisons(lambda time: time.datetime)
class Time:
    """ Simplify datetime, truncating seconds and microseonds for now. """
    timezone = "Europe/Paris"
    format = "%Y-%m-%d %H:%M %Z"

    def __init__(self, time):
        if isinstance(time, Time):
            time = time.datetime
        else:
            if isinstance(time, str):
                time = parser.parse(time, tzinfos={"CET": gettz("CET"), "CEST": gettz("CEST")})
            if str(time.tzinfo) != self.timezone:
                time = time.astimezone(self.get_timezone_obj())
            time = time.replace(second=0, microsecond=0)

        self.datetime = time

    @classmethod
    def get_timezone_obj(cls):
        return pytz.timezone(cls.timezone)

    @classmethod
    def now(cls):
        return Time(datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(cls.get_timezone_obj()))

    def __sub__(self, other):
        difference = self.datetime - Time(other).datetime
        return difference.total_seconds()

    def __str__(self):
        return self.datetime.strftime(self.format)

    def __repr__(self):
        return repr(self.datetime)












































