def extract_nth(test_list,n):
    result= list(map(lambda x:(x[n]),test_list))
    return result
students =[('grey',98,99),('brady',97,96),('wyatt',91,94)]
print(students)
n=2
print(extract_nth(students,n))
