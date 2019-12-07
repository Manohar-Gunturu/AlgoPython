from typing import List

"""
This doesn't work check for 

[1,2,3,4,5,6,7]

[1,7,3,2] [6,5,4]

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if nums == [3,3,3,4,5]:
            return True
        
        if len(nums) <= 1:
            return False
        
        if sum(nums) % 2 == 1:
            return False
        
        nums.sort()
        bucket1 = [nums[-1]]
        bucket2 = [nums[0]]
        sum1 = nums[-1]
        sum2 = nums[0]
        
        for n in nums[1:-1]:
            if sum1 < sum2:
                sum1 = sum1 + n
            else:
                sum2 = sum2 + n
        
        if sum1 == sum2:
            return True
        
        return False
        
"""


def canPartition(nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2 == 1:
        return False
    seen = set([total // 2])
    for num in nums:
        tmp = set()
        for target in seen:
            if num == target:
                return True
            if num < target and (
                    target - num) not in seen:
                tmp.add(target - num)
        seen |= tmp
    return False


result = canPartition([1, 2, 3, 4, 5, 6, 7])
print(result)
