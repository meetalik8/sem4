#Tuples
mytyple=(1,2,3,4,5)
print(mytyple)
print(len(mytyple))
print(mytyple[-1])
y=list(mytyple)
y[1]="kiwi"
mytyple=tuple(y)
print(mytyple)
num=mytyple+mytyple
print(num)