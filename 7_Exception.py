def division(a,b):
    try:
        c=a/b
    except Exception as err:
        print(err)
    else:
        print(c)
    finally:
        print("rest of the code")
division(3,4)
division(2,0)

mylist=(1,2,3,4)
try:
    x=mylist[4]
    #print(x)
except Exception as err:
    print(err)
else:
    print(x)
finally:
    print("rst of the code")
    
