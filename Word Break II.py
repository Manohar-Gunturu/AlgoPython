from typing import List


def wordBreak(s: str, wordDict: List[str]) -> List[str]:

    def helper(start, end, gtmp, result=[]):

        if start >= end:
            result.append(gtmp)
            return None

        for i in range(start, end):
            if s[start: i + 1] in wordDict:
                tmp = gtmp + " " + s[start: i + 1]
                helper(i + 1, end, tmp, result)
                tmp = gtmp

        return result

    return helper(0, len(s), "", [])


result = wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])
print(result)
