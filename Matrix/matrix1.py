n = int(input())
mat=[]
arr=[]
for i in range(n):
    row = list(map(int,input().split()))
    mat.append(row)

for i in range(n):
    for j in range(n):
        if j < n-3:
            if mat[i][j]== mat[i][j+1] == mat[i][j+2]==mat[i][j+3]:
                arr.append(mat[i][j])
        if i < n-3:
            if mat[i][j]== mat[i+1][j] == mat[i+2][j]==mat[i+3][j]:
                arr.append(mat[i][j])

        if i>=3 and j< n-3:
            if mat[i][j] == mat[i-1][j+1] == mat[i-2][j+2] == mat[i-3][j+3]:
                arr.append(mat[i][j])

        if j <n-3 and i < 2:
            if mat[i][j] == mat[i + 1][j + 1] == mat[i + 2][j + 2] == mat[i + 3][j + 3]:
                arr.append(mat[i][j])

print(arr)