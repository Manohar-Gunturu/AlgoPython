# divide and conquer
from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        return self.divide(nums, 0, len(nums) - 1)

    def divide(self, nums, i, j):
        if i >= j:
            return nums[i]

        mid = (i + j) // 2

        left = self.divide(nums, i, mid)
        right = self.divide(nums, mid + 1, j)
        cross_sum = self.cross_sum(nums, i, j, mid)
        return max(left, right, cross_sum)

    def cross_sum(self, nums, i, j, mid):

        max_left = nums[mid]
        sum_left = nums[mid]
        for i1 in range(mid - 1, i - 1, -1):
            max_left = max(max_left, sum_left + nums[i1])
            sum_left = sum_left + nums[i1]

        max_right = nums[mid + 1]
        sum_right = nums[mid + 1]

        for i1 in range(mid + 2, j + 1, 1):
            max_right = max(max_right, sum_right + nums[i1])
            sum_right = sum_right + nums[i1]

        return max_right + max_left


max_sub_array = Solution()
result = max_sub_array.maxSubArray([2, 5, -2, 3, 2, 1])
print(result)