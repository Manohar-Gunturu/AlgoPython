from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:

        tracker = dict()
        for i, em in enumerate(row):
            tracker[em] = i

        swaps = 0
        i = 0
        while i < len(row):
            em = row[i]
            pair = row[i + 1]
            if (em % 2 == 0 and pair != em + 1) or (em % 2 != 0 and pair != em - 1):
                # then do a swap
                real_mate = em + 1 if (em % 2 == 0) else em - 1
                # find the position of real mate
                row[tracker[real_mate]], row[i + 1] = row[i + 1], row[tracker[real_mate]]
                # update tracking
                tracker[pair] = tracker[real_mate]
                swaps += 1
                print(row)
            i += 2
        print(swaps, row)
        return swaps


s = Solution()
s.minSwapsCouples([0, 2, 4, 6, 7, 1, 3, 5])
