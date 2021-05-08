def staircase(n):

    if n == 1:
        return 1
    if n == 2:
        return 2

    return staircase(n-1) + staircase(n-2)


print(staircase(3))



def staircase_dp(n,memo = {}):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n == 2:
        return 2

    memo[n] = staircase(n - 1) + staircase(n - 2)
    return memo[n]


print(staircase_dp(5))