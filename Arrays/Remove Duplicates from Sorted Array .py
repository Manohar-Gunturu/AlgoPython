from typing import List


def removeDuplicates(nums: List[int]) -> int:
    i = 0
    j = 0
    tmp = 0
    while i < len(nums):

        tmp = nums[i]
        nums[j] = nums[i]
        j += 1
        i += 1
        if i < len(nums) and tmp == nums[i]:
            nums[j] = nums[i]
            j += 1
            i += 1

        while i < len(nums) and tmp == nums[i]:
            i += 1

    print(nums, j)


removeDuplicates([0, 0, 0, 0, 1, 1, 1, 1, 2, 3, 3])
