import math

from typing import List
"""

"""

class Box:
    def __init__(self):
        self.max_element = -float('inf')
        self.min_element = float('inf')
        self.used = False


class Solution:

    def maximumGap(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        max_element = max(nums)
        min_element = min(nums)

        boxes = []

        # bucket size:
        # gap between elements in each bucket < max_gap
        b_size = math.ceil((max_element - min_element) / (len(nums) - 1))

        if b_size == 0:
            return 0

        no_of_boxes = math.ceil((max_element - min_element) / b_size)

        # i = min_element
        for b in range(no_of_boxes + 1):
            boxes.append(Box())
            # i = b_size + (i)

        for element in nums:
            box = boxes[(element - min_element) // b_size]
            if box.min_element > element:
                box.min_element = element
            if box.max_element < element:
                box.max_element = element

        max_gap = 0
        previous_box_max = boxes[0].max_element
        for box in boxes[1:]:
            if not box.used:
                continue
            if box.min_element - previous_box_max > max_gap:
                max_gap = box.min_element - previous_box_max
            previous_box_max = box.max_element

        return max_gap


s = Solution()

s.maximumGap([1, 1, 1, 1, 1, 5, 5, 5, 5, 5])
