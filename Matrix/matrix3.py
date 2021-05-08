m = int(input())
n = m+1
MAT = []
arr = []
for i in range(m):
    row = list(map(int,input().split(' ')))
    MAT.append(row)

print(MAT)
for i in range(m):
    for j in range(n):
        print(MAT[i][j],end = " ")
    print()
for i in range(m):
    for j in range(n):
        print("*", i, j)
        if j <= n - 3:
            if MAT[i][j] == MAT[i][j+1] == MAT[i][j+2] :
                arr.append(MAT[i][j])

        if i <= m-3:
            if MAT[i][j] == MAT[i+1][j] == MAT[i+2][j]:
                arr.append(MAT[i][j])

        if i >= 3 and j <= n - 3:
            if MAT[i][j] == MAT[i-1][j+1] == MAT[i-2][j+2]:
                arr.append(MAT[i][j])

        if i <= m - 3 and j <= n-3:
            if MAT[i][j] == MAT[i+1][j+1] == MAT[i+2][j+2] :
                arr.append(MAT[i][j])

print(arr)
