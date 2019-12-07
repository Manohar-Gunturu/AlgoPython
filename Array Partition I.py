import math
from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        arr = [0 for i in range(0, 21)]
        step = 10
        for num in nums:
            arr[num + step] = arr[num + step] + 1

        i = -10
        total_sum = 0
        flag = 0
        while i <= 10:
            freq = arr[i + step] - flag
            total_sum = total_sum + math.ceil(freq / 2) * i
            flag = freq % 2
            i = i + 1

        return total_sum


s = Solution()
result = s.arrayPairSum([1, 1, 3, 1, 3, 3])
print(result)
