from math import inf
from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [0] * (amount + 1)
        for a in range(1, amount + 1):
            m = inf
            for c in coins:
                if c <= a:
                    m = min(arr[a - 1] + 1, m)

            arr[a] = m


s = Solution()
print(s.coinChange([1, 2, 5], 11))
