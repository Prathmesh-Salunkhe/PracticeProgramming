def visited(grid, row, col,memo = {}):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return
    if grid[row][col] == 0:
        return

    grid[row][col] = 0

    trav = [(row - 1, col), (row, col - 1), (row, col + 1), (row + 1, col)]

    for r, c in trav:
        visited(grid, r, c)

    return


def count_island(gird):
    count = 0

    for row in range(len(grid)):
        for col in range(len(gird[0])):
            if grid[row][col] == 1:
                count += 1
                visited(grid, row, col,memo = {})

    return count


if __name__ == '__main__':

    n = int(input())
    grid = []
    for i in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    max_count = count_island(grid)
    print(max_count)

# sample input
# 5
# 1 0 0 1 1 1
# 1 0 1 0 0 1
# 0 0 0 0 0 0
# 1 1 0 0 0 0
# 1 0 0 0 0 0
