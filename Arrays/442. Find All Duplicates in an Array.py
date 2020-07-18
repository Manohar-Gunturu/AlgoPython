from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 1
        dups = []

        if len(nums) == 1:
            return []

        nums.insert(0, 0)

        while i < len(nums):
            r = nums[i]

            if i != r and nums[i] == nums[r]:
                dups.append(r)
            else:
                nums[i], nums[r] = nums[r], nums[i]
            i += 1
            print(nums)
        return dups


f = Solution().findDuplicates([5,4,6,7,9,3,10,9,5,6])
print(f)
