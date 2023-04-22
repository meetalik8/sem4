word = "HeLlO WoRlD"
def calculate_upper_case(word):
    upper=0
    lower=0
    for i in word:
        if i.isupper():
            upper=upper+1
        else:
            lower=lower+1
    return(print("upper case is ",upper," LOWER CASE IS ",lower))
calculate_upper_case(word)
