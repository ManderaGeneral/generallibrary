
from generallibrary import *


a = TreeDiagram()
b = TreeDiagram(parent=a)
c = TreeDiagram(parent=a)
d = TreeDiagram(parent=c)
e = TreeDiagram(parent=a)

print(a.view())

# HERE ** finish lanes

# ├
# ─
# │
# └
