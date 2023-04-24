def test_dup(array_nums):
    num_set= set(array_nums)
    return len(array_nums) != len(num_set)
print(test_dup([1,2,3,4,5]))
print(test_dup([1,1,2,2,3,3,4,4,5]))
