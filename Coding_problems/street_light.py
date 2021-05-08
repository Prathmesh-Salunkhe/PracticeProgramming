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


def streetLight(n,k):
    index = binaryindex(n-1)
    count = 0
    for idx in index:
        dist = 0
        flag = False
        for i in idx:
            if i == 1:
                dist = 0
            else:
                dist += 1
            if dist > k:
                flag = True
                break
        if flag is False:
            count += 1

    return count


n = int(input())
k = int(input())

print(streetLight(n,k))