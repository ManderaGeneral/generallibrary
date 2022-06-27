
from generallibrary import *

from generalpackager import Packager


# Packager().graph(name_func=lambda x: x.simple_name)

from generallibrary.code import Log, testing

import logging



stream = logging.StreamHandler()
logger = logging.getLogger()
logger.addHandler(stream)
logger.setLevel(10)

testing()

a = Log("generallibrary.hi.test")  # HERE ** Add tests for Log and comment or fix that spawn_children only works for initial avaialable loggers






