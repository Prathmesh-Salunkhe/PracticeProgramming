def MinSubDiff(arr,n,total,sum1=0):
    if sum1 == total/2:
        return 0
    if n == 0:
        return sum(arr)-sum1
    if n<0:
        return 1000000

    return min(MinSubDiff(arr,n-1,total,sum1+arr[n]),MinSubDiff(arr,n-1,total,sum1))

def MinSubDiff_dp(arr,n,total,sum1=0,memo={}):
    if (n,sum1) in memo:
        return memo[(n,sum1)]
    if sum1 == total/2:
        memo[(n, sum1)] = 0
        return 0
    if n == 0:
        memo[(n, sum1)] = sum(arr)-sum1
        return sum(arr)-sum1
    if n<0:
        return 1000000

    memo[(n, sum1)] = min(MinSubDiff_dp(arr,n-1,total,sum1+arr[n],memo),MinSubDiff_dp(arr,n-1,total,sum1,memo))
    return memo[(n,sum1)]

if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        value = int(input())
        arr.append(value)
    total = sum(arr)
    print(MinSubDiff_dp(arr, len(arr) - 1,total))