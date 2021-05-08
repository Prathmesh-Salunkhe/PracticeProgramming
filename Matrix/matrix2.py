n = int(input())
row_zero = [False]*n
col_zero = [False]*n
arr = []
for i in range(n):
    rowno = list(map(int,input().split()))
    arr.append(rowno)

for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()

for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            row_zero[i]= True
            col_zero[j]= True

for row in range(len(row_zero)):
    if row_zero[row] == True:
        for j in range(n):
            arr[row][j] = 0
for col in range(len(col_zero)):
    if col_zero[col] == True:  #if col_zero[col] : this will do the job as it contaion true or false values
        for i in range(n):
            arr[i][col] = 0

for i in range(n):
    for j in range(n):
        print(arr[i][j] , end=" ")
    print()


