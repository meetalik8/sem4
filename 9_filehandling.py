f=open("demofile.txt","w")
f.write("Hello this is me writing in the file")
f=open("demofile.txt","r")
print(f.read())
f=open("demofile.txt","a")
f.write("\nI am now appending to it")
f=open("demofile.txt","r")
print(f.read())
f.close()
