def countSubsetDifference(arr,total,diff,n,sum1 = 0):
    if diff == total - 2*sum1:
        return 1
    if n <= 0 :
        return 0
    count = 0
    count += countSubsetDifference(arr,total,diff,n-1,sum1 + arr[n]) + countSubsetDifference(arr,total,diff,n-1,sum1)

    return count


if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        value = int(input())
        arr.append(value)
    diff = int(input())
    total =sum(arr)
    print(countSubsetDifference(arr,total,diff, len(arr) - 1))