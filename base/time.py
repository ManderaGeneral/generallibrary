
import time

class Timer:
    """
    Callable class to easily time things and print
    """
    def __init__(self, startTime=None):
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

def sleep(seconds):
    """
    Could do a sweet loading animation in console
    """
    time.sleep(seconds)



from base.types import typeChecker
