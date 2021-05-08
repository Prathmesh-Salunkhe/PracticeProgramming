def staircase(n, k):
    if n == 0:
        return 1
    if n < 0:
        return 0

    count = 0
    for i in range(1, k + 1):
        count += staircase(n - i, k)

    return count


print(staircase(5, 1))

def staircase_dp(n, k,memo = {}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    if n < 0:
        return 0

    count = 0
    for i in range(1, k + 1):
        count += staircase(n - i, k)

    memo[n] = count
    return count


print(staircase_dp(5, 1))


