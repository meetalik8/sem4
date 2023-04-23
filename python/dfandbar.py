import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a=np.array([[4,8,5,7,6],[2,3,4,2,6],[4,7,4,7,8],[2,6,4,8,6],[2,4,3,3,2]])
df=pd.DataFrame(a,columns=['a','b','c','d','e'],index=[2,4,6,8,10])
df.plot(kind='bar')
plt.show()
