
from generallibrary import *


class X(TreeDiagram):
    shared = ...  # For type hinting

    def _set_shared(self):
        self.shared = self.get_parent().shared if hasattr(self.get_parent(), "shared") else {}

hook(X.set_parent, X._set_shared, owner=X, after=True)


a = X()
b = X(parent=a)


a.shared["a"] = 3

print(b.shared)
print(X.shared)














