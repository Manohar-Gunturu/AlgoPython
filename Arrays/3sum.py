import collections
import bisect
from typing import List


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # print(nums[-1])
        counts = collections.defaultdict(int)
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

        nums = sorted(counts)

        # print(nums)
        for i, num in enumerate(nums):
            if counts[num] > 1:
                if num == 0:
                    if counts[num] > 2:
                        ans.append([num, num, num])
                else:
                    if -num * 2 in nums:
                        ans.append([num, num, -2 * num])

            if num < 0:
                twosum = -num
                # print(nums[-1])
                left = bisect.bisect_left(nums, (twosum - nums[-1]), i + 1)
                right = bisect.bisect_right(nums, (twosum // 2), left)
                # print("lr",twosum-nums[-1],(twosum//2),left,right)
                for i in nums[left:right]:
                    j = twosum - i
                    if j in counts and j != i:
                        ans.append([num, i, j])

        return ans


class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not len(nums):
            return []
        from collections import Counter
        from bisect import bisect_left
        count = Counter(nums)
        nums = sorted(count)
        ret = []
        for i, num_i in enumerate(nums[:bisect_left(nums, 0)]):
            jk_sum = -num_i
            end_num = (jk_sum + 1) // 2
            start = bisect_left(nums, jk_sum - nums[-1], i + 1)
            ret.extend((
                (num_i, num_j, jk_sum - num_j)
                for num_j in nums[start:bisect_left(nums, end_num, start)]
                if jk_sum - num_j in count))
        # triple zero
        if count.pop(0, 0) > 2:
            ret.append((0, 0, 0))
        # double
        ret.extend((
            (dup, dup, -2 * dup)
            for dup in filter(lambda x: count[x] > 1 and -2 * x in count, count)))
        return ret


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []
        for i, v in enumerate(nums):
            if v == nums[i - 1]:
                continue
            v = v
            low = i + 1
            high = len(nums) - 1
            while low < high:
                cval = nums[low] + nums[high]
                if v + cval == 0:
                    result.append([v, nums[low], nums[high]])

                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1

                    low = low + 1
                    high = high - 1
                elif v + cval > 0:
                    high -= 1
                else:
                    low += 1

        return result


s = Solution2()
s.threeSum([-5, 2, 3, 5])
#s.threeSum([-5, -2, -1, -2, 0, 1, 4, -1, 3, -4, 5,  6, 11])
