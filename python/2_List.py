#lists in python:

mylist=[1,2,3,4,5]
mylist.append(6)
print(mylist)
print(mylist[2])
print(len(mylist))

wordlist=["Taylor","Ella","Kacey","Jude","Maisie","Lana"]
print(wordlist[-3])
print(wordlist[2:5])
print(wordlist[:4])
print(wordlist[3:])
print(wordlist[-4:-1])
wordlist[2]="Twigs"
print(wordlist)
wordlist.append("Kacey")
print(wordlist)
wordlist.remove("Lana")
print(wordlist)
wordlist.pop(4)
print(wordlist)
wordlist.sort(reverse=True)
print(wordlist)


