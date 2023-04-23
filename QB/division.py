def division(a,b):
    try:
        c=a/b
        print(c)
    except Exception as err:
        print(err)
    finally:
        print("This function works")
a=int(input("enter num1: "))
b=int(input("enter num2: "))
division(a,b)
