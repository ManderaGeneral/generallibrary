
from generallibrary import *

from generalpackager import Packager


# Packager().graph(name_func=lambda x: x.simple_name)

from generallibrary.code import log

log().info("hi")
log().warning("hi")
log().critical("hi")

def x():
    log().info("hey")
    log().warning("hey")
    log().critical("hey")

x()