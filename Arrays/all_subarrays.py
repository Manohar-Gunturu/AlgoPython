from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s = 0
        d = {0: -1}
        for i in range(len(nums)):
            s = s + nums[i]

            if k != 0:
                s = s % k

            if s in d:
                if i - d[s] >= 2:
                    return True
            else:
                d[s] = i

        return False


Solution().checkSubarraySum([23, 2, 4, 6, 7], 6)
