from typing import List


class Solution:

    def diffWaysToCompute(self, input: str) -> List[int]:

        self.memo = {}
        self.ops = ["+", "-", "*"]
        return self.dp(input)

    def dp(self, input):

        if len(input) == 1:
            return input

        for i in range(0, len(input)):
            if i in self.ops:
                self.dp(input[:i])
                self.dp(input[i + 1:])

    def op(code, a_arr, b_arr):
        """

        @rtype: int
        """



s = Solution()
print(s.diffWaysToCompute('2-1-2*3'))
