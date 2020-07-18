from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # [1,2,3,4,5,6,7]
        # 1, 2, 3, 1, 5, 6, 7
        # 1, 2, 3, 1, 5, 6, 4
        # 1, 7, 3, 1, 5, 6, 4
        # 1, 7, 3, 1, 2, 6, 4
        # 5, 7, 3, 1, 2, 6, 4

        i, count = 0, 0
        while count < len(nums):
            newpos = (i + k) % len(nums)
            firstpos = newpos
            prev = i
            tmp = nums[i]
            while True:
                nums[newpos], tmp = tmp, nums[newpos]
                newpos = (newpos + k) % len(nums)
                print(nums)
                count += 1
                if newpos == firstpos:
                    break

            i = prev + 1


Solution().rotate([1, 2], 1)
