from typing import List


def subsets(nums: List[int]) -> List[List[int]]:

    result = []

    if len(nums) >= 1:
        result.append([nums[0]])

    for v in nums[1:]:

        for i in range(0, len(result)):
            result.append(result[i] + [v])

        result.append([v])

    result.append([])

    return result


result = subsets([1, 2, 3])
print(result)
