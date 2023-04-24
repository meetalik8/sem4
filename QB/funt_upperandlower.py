def upandlow(string):
    up=0
    low=0
    for i in string:
        if i.isupper():
            up+=1
        elif i.islower():
            low+=1
        else:
            pass
    return(print("The upper case is: ",up,"and lower is: ",low))
upandlow("hYOeyO")
