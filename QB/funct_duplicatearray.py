import array as ar
def test(nums):
    return sorted(set(nums),key=nums.index)
array_num = ar.array('i', [1, 3, 5, 1, 3, 7, 9])
print("Original array:")
for i in range(len(array_num)):
    print(array_num[i], end=' ')
print("\nAfter removing duplicate elements from the said array:")
result = ar.array('i', test(array_num))
for i in range(len(result)):
    print(result[i], end=' ')
