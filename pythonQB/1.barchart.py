#Write a Python programming to display a bar chart of the popularity of programming Languages.
#Programming languages: Java, Python, PHP, JavaScript, C#, C++
#Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
import matplotlib.pyplot as plt
x=['Java','Python','PHP','JS','C#','c++']
y=[22.2,17.6,8.8,8,7.7,6.7]
plt.bar(x,y)
plt.xlabel("Languages")
plt.ylabel('Popularity')
plt.show()

#horizontal
x=['Java','Python','PHP','JavaScript','C#','C++']
y=[22.2,17.6,8.8,8,7.7,6.7]
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.barh(x,y,color="green")
plt.show()

#different color for each bar
x=['Java','Python','PHP','JavaScript','C#','C++']
y=[22.2,17.6,8.8,8,7.7,6.7]
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.bar(x,y,color=['blue','green','red','pink','yellow','brown'])
plt.show()
