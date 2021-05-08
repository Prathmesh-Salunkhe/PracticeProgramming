
def coinSum(sum,coin):
    if sum == 0:
        return []
    if sum < 0:
        return None

    for c in coin:
        reminder = sum - c
        result = coinSum(reminder,coin)
        if result is not None:
            returnValue = result + [c]
            return returnValue

    return None


#print(coinSum(7,[2,3]))

def coinSum_dp(sum,coin,memo={}):
    if sum in memo:
        return memo[sum]
    if sum == 0:
        return []
    if sum < 0:
        return None

    for c in coin:
        reminder = sum - c
        result = coinSum_dp(reminder,coin,memo)
        if result is not None:
            memo[sum] = result + [c]
            return memo[sum]

    memo[sum] = None
    return None

print(coinSum_dp(7,[2,3]))
print(coinSum_dp(300,[7,14]))
