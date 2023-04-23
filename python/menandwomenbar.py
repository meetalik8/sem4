import matplotlib.pyplot as plt
import numpy as np
n=5
men=[22,30,35,35,26]
women=[25,32,30,35,29]
#x=["S1","S2","S3","S4","S5"]
bar_width=0.3
index=np.arange(n)
plt.xlabel("People")
plt.ylabel("Scores")
plt.xticks(index+bar_width,("S1","S2","S3","S4","S5"))
plt.bar(index,men,bar_width)
plt.bar(index+bar_width,women,bar_width)
plt.legend(["MEN","WOMEN"])
plt.title("Scores by persons")
plt.show()
