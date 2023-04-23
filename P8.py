import random
import string
print(random.choice(string.ascii_letters))

length=100
s=''
for i in range(random.randint(1,length)):
    s += random.choice(string.ascii_letters)
print(s)

print("String of specific length: ")
st=''
max_len=int(input("enter length: "))
for i in range(max_len):
    st+=random.choice(string.ascii_letters)
print(st)
