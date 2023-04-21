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
