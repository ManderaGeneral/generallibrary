
from generallibrary import *


class X(DataClass):
    foo: str = "bar"



print(X.field_dict_annotations())




