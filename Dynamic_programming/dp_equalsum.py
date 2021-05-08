def equalsum(arr,a=[],b=[]):
    if sum(a) == sum(b) and len(a) > 0 and len(b) > 0:
        return True

    for v in arr:
        a.append(v)
        arr.remove(v)
        if equalsum(arr,a,b):
            return True
        a.remove(v)
        arr.append(v)

        b.append(v)
        arr.remove(v)
        if equalsum(arr,a,b):
            return True

    return False


if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        v = int(input())
        arr.append(v)

    print(equalsum(arr))