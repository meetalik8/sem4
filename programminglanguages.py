import matplotlib.pyplot as plt
x=['Java','Python','PHP','JS','C#','C++']
y=[22.2,17.6,8.8,8,7.7,6.7]
plt.xlabel("Languages")
plt.ylabel("popularity")
bar_width=0.4
plt.bar(x,y,bar_width,color=["r","g","b","k","y","c"])
plt.show()

##horizontal
plt.xlabel("Languages")
plt.ylabel("popularity")
plt.barh(x,y,bar_width)
plt.show()

##pie
myexplode=[0.1,0,0,0,0,0]
plt.pie(y,labels=x,startangle=90,explode=myexplode,autopct='%1.1f%%')
plt.show()

##pie with title
plt.pie(y,labels=x,autopct="%1.1f%%")
plt.title("Popularity of programming languages")
plt.show()
