import numpy as np
a= np.arange(1,10).reshape(3,3)
print(a)
print(np.linalg.norm(a,'fro'))
