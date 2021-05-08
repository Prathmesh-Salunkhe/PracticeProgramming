def coinSum(n,coin):
    if n == 0:
        return True
    if n < 0:
        return False
    if n < min(coin):
        return False

    for c in coin:
        subonecoin = n - c
        if coinSum(subonecoin,coin):
            return True

    return False

#print(coinSum(7,[2,2]))

def coinSum_dp(n,coin, memo = {}):
    if n in memo:
        return memo[n]
    if n == 0:
        return True
    if n < 0:
        return False
    if n < min(coin):
        return False

    for c in coin:
        subonecoin = n - c
        memo[n] = coinSum_dp(subonecoin,coin,memo)
        if memo[n]:
            return True

    memo[n] = False
    return memo[n]

print(coinSum_dp(300,[7,14]))