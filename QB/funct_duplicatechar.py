def duplicate_letters(text):
    word_list=text.split()
    for word in word_list:
        if len(word)>len(set(word)):
            return False
    return True
text = 'Filter out the factorials of the said list.'
print("Original text:")
print(text)
print("Check whether any word in the said sting contains duplicate characrters or not!")
print(duplicate_letters(text))
