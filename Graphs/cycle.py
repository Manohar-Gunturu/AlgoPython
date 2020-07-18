from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inde = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[v].append(u)
            inde[u] += 1
        stack = []
        for i in range(numCourses):
            if inde[i] == 0:
                stack.append(i)
        count = 0
        while stack:
            u = stack.pop()
            count += 1
            for v in graph[u]:
                inde[v] -= 1
                if inde[v] == 0:
                     stack.append(v)
        return True if count == numCourses else False


s = Solution()
s.canFinish(4, [[1, 0], [1, 2], [3, 0], [0, 2]])
