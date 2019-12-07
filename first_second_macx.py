from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        first_max = second_max = nums[0]
        first_min = second_min = nums[0]

        for val in nums:

            if val > first_max:
                second_max = first_max
                first_max = val

            if val < first_min:
                second_min = first_min
                first_min = val

            if first_min < val < second_min:
                second_min = val

            if first_max > val > second_max:
                second_max = val

        if len(nums) == 2:
            return first_min
        else:
            return first_min + second_max


s = Solution()
result = s.arrayPairSum([1, 1, 2, 2])
print(result)