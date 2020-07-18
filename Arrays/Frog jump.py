from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1 or nums.count(0) == 0:
            return True

        if nums[0] == 0:
            return False

        indices = [i for i, x in enumerate(nums) if x == 0]

        for n in range(len(nums) - 1):
            nums[n] += n

        for i in indices:
            if i > len(nums) - 1:
                return True
            # think like can you pass this hole
            if (max(nums[0:i])) <= nums[i]:
                return False

        return True


s = Solution()
s.canJump([3,2,1,0,4])