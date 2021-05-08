def countSum(arr,total,n):
    if total == 0:
        return 1
    if n < 0:
        return 0
    if total < 0:
        return 0

    return countSum(arr,total-arr[n],n-1)+countSum(arr,total,n-1)

def countSum_dp(arr,total,n,memo={}):
    if (total,n) in memo:
        return memo[(total,n)]
    if total == 0:
        return 1
    if n < 0:
        return 0

    if total < 0:
        return 0

    memo[(total,n)] = countSum_dp(arr,total-arr[n],n-1,memo)+countSum_dp(arr,total,n-1,memo)
    return memo[(total,n)]


if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        value = int(input())
        arr.append(value)
    total = int(input())
    print(countSum_dp(arr,total,len(arr)-1))

