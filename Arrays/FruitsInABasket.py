from typing import List


class Solution:
    def totalFruit(self, tree: List[int]) -> int:

        last_fruit = -1
        last_s_fruit = -1
        last_fruit_c = 0
        count = 0
        max_count = 0

        for fruit in tree:

            # means we saw new kind of fruit
            if fruit != last_fruit and fruit != last_s_fruit:
                last_s_fruit = last_fruit
                last_fruit = fruit
                count = last_fruit_c + 1
                last_fruit_c = 0
            else:
                count = count + 1

                if fruit != last_fruit:
                    last_s_fruit = last_fruit
                    last_fruit = fruit
                    last_fruit_c = 0

            if fruit == last_fruit:
                last_fruit_c += 1

            max_count = max(max_count, count)

        return max_count


s = Solution()
print(s.totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
