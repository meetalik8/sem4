#Control Structures

#even and odd
num=int(input("Enter a number:"))
if(num%2==0):
    print("Even")
else:
    print("Odd")
num=int(input("Enter a number:"))
for i in range(1,num+1):
    if(i%2==0):
        print(i," is even\n")
    else:
        print(i," is odd")

#factorial
num=int(input("Enter a number:"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)

#palindrome
word=input("Enter a string: ")
reverse=word[::-1]
if(word==reverse):
    print("String is a palindrome")
else:
    print("String is not a palindrome")


