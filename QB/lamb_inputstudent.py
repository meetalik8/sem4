students=[]
names=[]
sec_low=[]
n=int(input("No. of students: "))
for _ in range(n):
    s_name=input('Name: ')
    score=float(input('Score: '))
    students.append([s_name,score])
print(students)

order= sorted(students,key=lambda x:int(x[1]))
for i in range(n):
    if order[i][1]!=order[0][1]:
        second_low=order[i][1]
        break
print("\nSecond lowest: ",second_low)
sec_student_name=[x[0] for x in order if x[1]==second_low]
sec_student_name.sort()

for s_name in sec_student_name:
    print(s_name)
