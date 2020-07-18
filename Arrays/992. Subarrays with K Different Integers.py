from collections import OrderedDict
from typing import List


class Solution1:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        from collections import defaultdict
        window1 = defaultdict(int)
        window2 = defaultdict(int)
        i = 0
        result = 0
        left = 0

        while i < len(A):

            window1[A[i]] += 1

            if len(window1) >= K:
                print(A[left:i + 1])
                result = result + 1

            i += 1

        return result


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        Kset = set()
        LatestIdx = OrderedDict()
        start = 0
        end = 0
        cnt = 0
        leN = len(A)
        while start < leN and end < leN:
            num = A[end]
            if num not in Kset:
                Kset.add(num)
                LatestIdx[num] = end
            else:
                del (LatestIdx[num])
                LatestIdx[num] = end

            if len(Kset) == K:
                miN = LatestIdx[next(iter(LatestIdx))]
                cnt += (miN - start + 1)
            elif len(Kset) > K:
                key, miN = LatestIdx.popitem(last=False)
                start = miN + 1
                Kset.remove(key)
                miN = LatestIdx[next(iter(LatestIdx))]
                cnt += (miN - start + 1)
            end += 1
        return cnt


s = Solution()
r = s.subarraysWithKDistinct([1, 2, 2, 1, 3, 3, 4, 4, 2, 5], 3)
print(r)
print("------------------------------------------")
# r = s.subarraysWithKDistinct([1, 2, 1, 2, 3], 2)
# print(r)

# r = s.subarraysWithKDistinct([2, 2, 1, 2, 2, 2, 1, 1], 2)
# print(r)
# 1, 2, 1, 3
# 2, 1, 3
# 1, 3, 4
# 3, 4, 2
# 4, 3, 5


# example 2:
# [1, 2, 1, 2, 3], K = 2
#  1 , 2 , 1
#  2, 1
#  2 , 1 , 2


# 2, 1, 2, 1, 3
