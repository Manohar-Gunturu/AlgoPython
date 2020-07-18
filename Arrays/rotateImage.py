from typing import List


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    i = 0
    j = len(matrix[0]) - 1
    rows = len(matrix) - 1

    while i < j:

        for k in range(i, j + 1):
            topleft = matrix[k][k]
            righttop = matrix[k][j]
            rightbottom = matrix[j][k]
            bottomleft = matrix[rows - k][k]

        i += 1
        j -= 1


a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate(a)
