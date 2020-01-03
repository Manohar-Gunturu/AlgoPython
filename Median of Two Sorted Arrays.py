from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        numOfelms = len(nums1) + len(nums2)
        median = []
        odd = True
        if numOfelms % 2 == 0:
            odd = False

        median.append(numOfelms // 2)

        l = 0
        r = 0
        curr = 0
        prev = 0
        while l < len(nums1) and r < len(nums2):

            prev = curr
            if nums1[l] > nums2[r]:
                curr = nums2[r]
                r = r + 1
            elif nums1[l] < nums2[r]:
                curr = nums1[l]
                l = l + 1
            else:
                curr = nums2[r]
                r = r + 1

            if l + r - 1 >= median[0]:
                if not odd:
                    return (prev + curr) / 2
                else:
                    return curr

        while l < len(nums1):
            prev = curr
            curr = nums1[l]
            l = l + 1
            if l + r - 1 == median[0]:
                if not odd:
                    return (prev + curr) / 2
                else:
                    return curr

        while r < len(nums2):
            prev = curr
            curr = nums2[r]
            r = r + 1
            if l + r - 1 == median[0]:
                if not odd:
                    return (prev + curr) / 2
                else:
                    return curr


s = Solution()
result = s.findMedianSortedArrays([1, 2], [1, 2, 3])
print(result)
