import numpy as np
import random
import string
print("\nHex color")
print("#{:06x}".format(random.randint(0,0xFFFFFF)))

max_len=255
s=''
for i in range(random.randint(1,max_len)):
    s+=random.choice(string.ascii_letters)
print("\nrandom string")
print(s)

print("\nRandom value between 1 and 100")
print(random.randint(1,100))

print("\nRandom multiples of 7 between 0 and 70")
print(random.randint(0,70)*7)
