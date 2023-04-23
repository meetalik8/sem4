import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a)

u,s,v = np.linalg.svd(a)
print(u)
print(s)
print(v)
