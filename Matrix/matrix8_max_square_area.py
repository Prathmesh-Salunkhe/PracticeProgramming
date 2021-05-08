def GetArea(grid,row,col):
    edge = 1
    while True:
        if row + edge >= len(grid) or col + edge >= len(grid[0]):
            break
        if grid[row + edge][col] == 1 and grid[row][col+edge] == 1:
            edge += 1
        else:
            break

    side = 1
    while side< edge:
        if grid[row+side][col+side] == 1:
            side +=1
        else:
            break
    # if we need to count the numbers insde square( if not only 1)
    # area = 0
    # for r in range(row,row+side):
    #     for c in range(col,col+side):
    #         area += grid[r][c]
    #


    area = side**2
    return area


def MaxArea(grid):
    area = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                sq_area = GetArea(grid,row,col)
                area = max(area,sq_area)


    return area



if __name__ == '__main__':

    n = int(input())
    grid = []
    for i in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    max_area = MaxArea(grid)
    print(max_area)
