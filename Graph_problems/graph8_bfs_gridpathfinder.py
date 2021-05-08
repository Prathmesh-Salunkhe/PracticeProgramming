def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                return i, j


def find_neighbours(r, c):
    direction = [(r, c - 1), (r, c + 1), (r + 1, c), (r - 1, c)]
    ngbh = []

    for row, col in direction:
        if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] != '#':
            ngbh.append((row, col))

    return ngbh


def path_travel(grid):
    visited = {}
    q = []
    parent = {}
    found = False
    r_start, c_start = find_start(grid)
    #print(r_start, c_start)

    q.append((r_start, c_start))
    visited[(r_start, c_start)] = True
    parent[(r_start, c_start)] = None

    while len(q) > 0 and found is False:
        r, c = q.pop(0)
        neighbours = find_neighbours(r, c)
        #print(r,c,neighbours)

        for row, col in neighbours:
            if (row, col) not in visited:
                visited[(row, col)] = True
                q.append((row, col))
                parent[(row, col)] = (r, c)
                if grid[row][col] == 'E':
                    found = True

    path = []
    child = (row, col)
    while child is not None:
        path.append(child)
        child = parent[child]

    path.reverse()

    return path


def make_path(grid,path):
    for row,col in path:
        grid[row][col] = '*'

    return grid



if __name__ == "__main__":
    n = int(input())
    graph = {}
    grid = []
    for i in range(n):
        row = list(input().split())
        grid.append(row)

    # print(grid)
    path = path_travel(grid)
    print(path)

    path_grid = make_path(grid,path)

    for i in range(n):
        print(path_grid[i])

# sample input:
# 4
# 0 S # 0 # #
# # 0 0 0 # 0
# 0 0 # 0 # E
# # 0 0 0 0 0
