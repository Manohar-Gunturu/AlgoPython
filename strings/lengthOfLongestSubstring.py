class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        i = 0
        j = 0
        length = 0

        # a b b a
        while i < len(s):

            if s[i] in seen:
                length = max(i - j, length)
                j = max(j, seen[s[i]] + 1)

            seen[s[i]] = i
            i += 1

        return max(length, i - j)


r = Solution().lengthOfLongestSubstring("tmmzuxt")
print(r)