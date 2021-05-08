def MinPathCost(grid,row = 0,col = 0,cost = 0):
    if row == len(grid) -1 and col == len(grid[0]) -1:
        return grid[row][col]

    if row >= len(grid) or col >= len(grid[0]):
        return 1000000


    cost += grid[row][col] + min(MinPathCost(grid,row + 1,col,cost),MinPathCost(grid,row,col+1,cost))

    return cost

def MinPathCost_dp(grid,row = 0,col = 0,cost = 0,memo = {}):
    if (row,col) in memo:
        return memo[(row,col)]

    if row == len(grid) -1 and col == len(grid[0]) -1:
        return grid[row][col]

    if row >= len(grid) or col >= len(grid[0]):
        return 1000000


    cost += grid[row][col] + min(MinPathCost_dp(grid,row + 1,col,cost,memo),MinPathCost_dp(grid,row,col+1,cost,memo))

    memo[(row,col)] = cost
    return cost


if __name__ == '__main__':

    n = int(input())
    grid = []
    for i in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    min_cost = MinPathCost(grid)
    print(min_cost)

# sample input
# 3
# 1 2 3 4
# 3 1 2 3
# 1 2 1 2