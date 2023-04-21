string=input("Enter a string: ")
print(string)
rev=string[::-1]
print(rev)
if(string==rev):
    print("Palindrome")
else:
    print("Not a palindrome")
