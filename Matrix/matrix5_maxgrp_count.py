def group_count(grid,row,col):
    if row < 0 or col < 0 or row >=len(grid) or col >=len(grid[0]):
        return 0

    if grid[row][col] == 0:
        return 0

    count = 1
    grid[row][col] = 0

    for r in range(row -1,row +2):
        for c in range(col -1,col +2):
            count += group_count(grid,r,c)


    return count

def count_group(grid):
    max_count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                grp_count = group_count(grid,row,col)
                max_count = max(max_count,grp_count)

    return max_count


if __name__ == '__main__':

    n = int(input())
    grid = []
    for i in range(n):
        row = list(map(int,input().split()))
        grid.append(row)

    max_count = count_group(grid)
    print(max_count)



#sample input
# 5
# 1 0 0 1 1 1
# 1 0 1 0 0 1
# 0 0 0 0 0 0
# 1 1 0 0 0 0
# 1 0 0 0 0 0