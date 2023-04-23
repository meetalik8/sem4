import numpy as np
p = [[1, 0], [0, 1]]
q = [[1, 2], [3, 4]]

result=np.dot(p,q)
print('matrix multi\n',result)

result=np.cross(p,q)
print("cross: \n",result)

result=np.outer(p,q)
print('outer\n',result)

a=np.array([1,2,3])
b=np.array([4,5,6])
result=np.einsum("n,n",a,b)
print('einstien summation\n',result)

result=np.linalg.det(p)
print('determinant\n',result)

result=np.trace(p)
print('sum of diagonal\n',result)
