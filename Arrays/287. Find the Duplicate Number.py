from typing import List


# CHAMPESADU PO, GO AND GET THE JOB AT GOOGLE ANd FACEBOOK
# This also can be used to sort
def findDuplicate(nums: List[int]) -> int:
    i = nums[0]
    while nums[i] != i:
        nums[i], i = i, nums[i]
        print(nums)
    return i


# IDEA 2: Change elements to negative and if negative found while chaning to negative then stop


# Binary search


g = findDuplicate([1, 2, 3, 4, 1])
print(g)
