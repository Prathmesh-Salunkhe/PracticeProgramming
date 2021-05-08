def coinSumMinCoin(coin, n, total):
    if total == 0:
        return 0

    if n < 0:
        return 10000000

    if total < 0:
        return 10000000

    return min(1 + coinSumMinCoin(coin, n, total - coin[n]), coinSumMinCoin(coin, n - 1, total))


if __name__ == "__main__":
    n = int(input())
    coin = []
    for i in range(n):
        c = int(input())
        coin.append(c)

    total = int(input())

    print(coinSumMinCoin(coin, len(coin) - 1, total))
