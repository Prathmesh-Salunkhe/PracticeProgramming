m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

for row in m:
    print(row)

for i in range(len(m)//2):
    for j in range(len(m[0])):
        #print(i,j,len(m[0])-1-i)
        m[j][(len(m[0])//2)+i] = m[j][i] + m[j][(len(m[0])//2)+i]
        #print(m[j][i],m[j][len(m[0])-1-i])


for row in m:
    print(row)
