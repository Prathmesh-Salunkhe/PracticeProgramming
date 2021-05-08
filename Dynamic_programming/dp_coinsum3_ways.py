def coinSumWays(coin,n,total,sum = 0):
    if total-sum == 0:
        return 1
    if sum>total:
        return 0
    if n<0:
        return 0

    count = 0
    count += coinSumWays(coin,n,total,sum + coin[n]) + coinSumWays(coin,n-1,total,sum)

    return count

def coinSumWays_dp(coin,n,total,sum = 0,memo = {}):
    if (n,sum) in memo:
        return memo[(n,sum)]
    if total-sum == 0:
        return 1
    if sum>total:
        return 0
    if n<0:
        return 0

    count = 0
    count += coinSumWays_dp(coin,n,total,sum + coin[n],memo) + coinSumWays_dp(coin,n-1,total,sum,memo)

    memo[(n, sum)] = count
    return count

if __name__ == "__main__":
    n = int(input())
    coin = []
    for i in range(n):
        c = int(input())
        coin.append(c)

    total = int(input())

    print(coinSumWays_dp(coin,len(coin)-1,total))