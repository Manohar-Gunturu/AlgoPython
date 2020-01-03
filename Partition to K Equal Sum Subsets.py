from typing import List


class Solution:

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        sumOfnums = sum(nums)
        bucketSum = sumOfnums / k

        if k > len(nums) or not bucketSum.is_integer():
            return False

        nums.sort()
        i = 0
        j = len(nums) - 1
        trackSum = 0
        tmp = 0
        while i < j:

            if nums[i] == bucketSum:
                i += 1
                tmp += 1
            elif nums[j] == bucketSum:
                j -= 1
                tmp += 1
            elif nums[i] + nums[j] == bucketSum:
                i += 1
                j -= 1
                tmp += 1
            elif trackSum + nums[i] == bucketSum:
                i += 1
                trackSum = 0
                tmp += 1
            else:
                trackSum = trackSum + nums[j]
                j -= 1

            if trackSum == bucketSum:
                trackSum = 0
                tmp += 1

        return True if tmp == k else False


s = Solution()
s.canPartitionKSubsets([10, 10, 10, 7, 7, 7, 7, 7, 7, 6, 6, 6], 3)
