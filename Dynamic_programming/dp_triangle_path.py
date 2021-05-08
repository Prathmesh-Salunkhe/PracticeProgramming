def trianglePath(triangle, row =0, col=0, min_path=0):
    if row == len(triangle) - 1:
        return triangle[row][col]


    value = min(trianglePath(triangle, row+1, col, min_path), trianglePath(triangle, row+1, col + 1, min_path)) + triangle[row][col]
    min_path += value

    return min_path

def trianglePath_dp(triangle, row =0, col=0,memo = {}):
    if (row,col) in memo:
        return memo[(row,col)]
    if row == len(triangle) - 1:
        return triangle[row][col]

    memo[(row,col)] = min(trianglePath(triangle, row+1, col), trianglePath(triangle, row+1, col + 1)) + triangle[row][col]
    return memo[(row,col)]


n = int(input())
triangle = []
for i in range(n):
    r = list(map(int, input().split()))
    triangle.append(r)

print(triangle)

min_path = trianglePath_dp(triangle)

print(min_path)
# sample input
# 4
# 2
# 3 4
# 6 5 7
# 4 3 2 1
