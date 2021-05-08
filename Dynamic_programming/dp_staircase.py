def streetlight(n,k,memo = {}):
    if n in memo:
        return memo[n]

    if k == 0:
        return 1
    if n == 0:
        return 1

    if n < 0:
        return 0

    count = 0

    for i in range(1,k+1+1):
        count += streetlight(n-i,k)

    memo[n] = count
    return count


n = int(input())
k = int(input())

print(streetlight(n,k))