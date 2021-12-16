
from generallibrary import *


class X(TreeDiagram):
    _shared = ...  # For type hinting

    def _set_shared(self):
        self._shared = self.get_parent()._shared if hasattr(self.get_parent(), "_shared") else {}

hook(X.set_parent, X._set_shared, owner=X, after=True)

a = X()
b = X(parent=a)


a._shared["a"] = 3

print(b._shared)
print(X._shared)














