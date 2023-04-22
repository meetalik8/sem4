import matplotlib.pyplot as plt
import numpy as np
n=5
men=[22,30,35,35,26]
women=[25,32,30,35,29]
mstd=[4,3,4,1,5]
wstd=[3,5,2,3,3]
x=["s1","s2","s3","s4","s5"]
plt.ylabel('Scores')
plt.xlabel('Groups')
plt.title('Scores by group and gender')
plt.bar(x,men,yerr=mstd)
plt.bar(x,women,bottom=men,yerr=wstd)
plt.show()
