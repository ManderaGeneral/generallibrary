from generallibrary.decorators import Operators
from generallibrary.context import DecoContext
from time import sleep as old_sleep
from datetime import datetime
import pytz
from dateutil import parser
from dateutil.tz import gettz
from timeit import default_timer


class Timer(DecoContext):
    TIMER_FUNC = default_timer
    UNIT = "seconds"

    def __init__(self, func, print_out=True):
        self.print_out = print_out
        self.start_time = self.before()

    def _prettify_time(self, time):
        """ Could do some unit conversion and stuff here. """
        return f"{time} {self.UNIT}"

    def time(self):
        time = self.TIMER_FUNC() - self.start_time
        if self.print_out:
            print(f"Time taken: {self._prettify_time(time=time)}")
        return time

    def before(self):
        self.start_time = self.TIMER_FUNC()
        return self.start_time

    def after(self):
        return self.time()


def sleep(seconds):
    """ Normal sleep function from time package.

        :param float seconds: Time in seconds to sleep. """
    old_sleep(seconds)


@Operators.deco_define_comparisons(lambda date: date.datetime)
class Date:
    """ Simplify datetime, truncating seconds and microseonds for now. """
    timezone = "Europe/Paris"
    format = "%Y-%m-%d %H:%M %Z"

    def __init__(self, date):
        if isinstance(date, Date):
            datetime_ = date.datetime
        else:
            if isinstance(date, str):
                datetime_ = parser.parse(date, tzinfos={"CET": gettz("CET"), "CEST": gettz("CEST")})
            else:
                datetime_ = date

            if str(datetime_.tzinfo) != self.timezone:
                datetime_ = self.get_timezone_obj().localize(datetime_.replace(tzinfo=None))

            datetime_ = datetime_.replace(second=0, microsecond=0)

        self.datetime = datetime_

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












































