
import time


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


