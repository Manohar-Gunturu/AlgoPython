from typing import List


def removeDuplicates(nums: List[int]) -> int:
    l = len(nums)
    i = 0
    j = 0
    while i < l:
        isLoop = False

        while i + 1 < l and nums[i] == nums[i + 1]:
            nums[j] = nums[i]
            isLoop = True
            i = i + 1

        if not isLoop:
            nums[j] = nums[i]

        i = i + 1
        j = j + 1

    return j


removeDuplicates([1, 1, 2])