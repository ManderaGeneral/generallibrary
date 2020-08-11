
import time

class Timer:
    """Callable class to easily time things and print."""
    def __init__(self, startTime=None):
        """
        Instantiate Timer which starts it.

        :param float startTime: Defaults to time in seconds since epoch (time.time())
        """
        if startTime is None:
            self.startTime = time.time()
        else:
            typeChecker(startTime, float)
            self.startTime = startTime

    def seconds(self):
        """
        :return: Seconds passed since timer started
        :rtype: float
        """
        return time.time() - self.startTime

    def print(self):
        """."""
        print(f"Seconds passed: {self.seconds()}")

def sleep(seconds):
    """
    Normal sleep function from time package.
    Stubbed for easy changing and whatnot.

    :param float seconds: Time in seconds to sleep.
    """
    time.sleep(seconds)


from generallibrary.types import typeChecker
