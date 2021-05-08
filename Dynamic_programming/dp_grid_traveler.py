def grid_traveler(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traveler(m - 1, n) + grid_traveler(m, n - 1)


print(grid_traveler(2, 3))
print(grid_traveler(3, 3))


def grid_traveler_dynamic(m, n, grid={}):
    key = str(m) + "," + str(n)
    if key in grid:
        return grid[key]

    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    grid[key] = grid_traveler_dynamic(m - 1, n, grid) + grid_traveler_dynamic(m, n - 1, grid)
    return grid[key]


print(grid_traveler_dynamic(18, 18))

