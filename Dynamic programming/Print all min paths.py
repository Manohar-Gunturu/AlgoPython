def find_all_shortest_paths(m, n):
    grid = [[0 for col in range(0, n)] for row in range(0, m)]

    for col in range(0, n):
        grid[m - 1][col] = 1

    for r in range(0, m):
        grid[r][0] = 1

    row = m - 2

    while row >= 0:
        for col in range(1, n):
            grid[row][col] = grid[row][col - 1] + grid[row + 1][col]

        row = row - 1

    print(grid)


find_all_shortest_paths(3, 4)
