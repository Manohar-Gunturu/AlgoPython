from typing import List


def minPathSum(self, grid: List[List[int]]) -> int:
    rows = len(grid)
    columns = len(grid[0])

    for i in range(0, rows):
        for j in range(0, columns):
            if i > 0 and j > 0:
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
            elif i > 0:
                grid[i][j] += grid[i - 1][j]
            elif j > 0:
                grid[i][j] += grid[i][j - 1]

    return grid[rows - 1][columns - 1]


minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
