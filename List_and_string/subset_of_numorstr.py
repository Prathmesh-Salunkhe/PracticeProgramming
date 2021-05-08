def binaryindex(n):
    index = []

    for i in range(2**n):
        idx = []
        number = i
        while number > 0:
            rem = number % 2
            idx.append(rem)
            number //= 2

        while len(idx) < n:
            idx.append(0)

        idx.reverse()
        index.append(idx)

    return index




def subsets(num):
    index = binaryindex(len(num))

    subset = []

    for i in range(len(index)):
        sub = []

        for j in range(len(index[i])):
            if index[i][j] == 1:
                sub.append(num[j])

        subset.append(sub)

    return subset






if __name__ == '__main__':
    n = int(input())
    num = []
    for i in range(n):
        num.append(int(input()))

    subset = subsets(num)
    print(subset)


#sample input
# 5
# 1
# 2
# 3
# 4
# 5