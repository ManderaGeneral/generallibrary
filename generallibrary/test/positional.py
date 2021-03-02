""" Dynamically ran by unittests if this python version supports positional-only args (3.8) """

from generallibrary.functions import SigInfo


def positional(self):
    """ :param unittest.TestCase self: """
    sigInfo = SigInfo(lambda x, /, y=2, b=4, *args, z=3, s, **kwargs: 5)
    self.assertEqual(["x", "y", "b", "args"], sigInfo.positionalArgNames)
    self.assertEqual(["z", "s", "kwargs"], sigInfo.positionalOppositeArgNames)

    self.assertEqual(["x", "args"], sigInfo.positionalOnlyArgNames)
    self.assertEqual(["y", "b", "z", "s", "kwargs"], sigInfo.positionalOnlyOppositeArgNames)

    self.assertEqual({"y": 2, "b": 4, "z": 3}, sigInfo.defaults)

    self.assertEqual(["x", "y"], SigInfo(lambda x, /, y: 5).namesRequired)
    self.assertEqual(["x", "y"], SigInfo(lambda x, /, y, z=2: 5).namesRequired)
    self.assertEqual(["x", "s"], SigInfo(lambda x, y=2, /, b=4, *args, z=3, s, **kwargs: None).namesRequired)

    self.assertEqual({"y": 2, "b": 4, "z": 3}, SigInfo(lambda x, y=2, /, b=4, *args, z=3, s, **kwargs: None).defaults)
