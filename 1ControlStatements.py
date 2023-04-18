#CONTROL STATEMENTS: LOOP STATEMENTS
#break, continue, pass,if-else

n=7
for i in range(n):
    if(i%2==0):
        print("Even",i)
    else:
        print("Odd",i)
for i in "Hello World":
    if(i == " "):
        continue
    print(i)
