for i in range(1,5):
    for j in range(1,5-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print(" ")
for i in range(1,5):
    for j in range(1,i+1):
        print(" ",end=" ")
    for k in range(1,5-i):
        print("*",end=" ")
    for m in range(1,5-i):
        print('*',end=" ")
    print(" ")
