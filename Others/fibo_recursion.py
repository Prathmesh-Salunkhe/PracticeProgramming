def fib(n):
    if n <= 2:
        return 1
    return fib(n - 2) + fib(n - 1)


print(fib(50))


# dynamic programming
def fib_dynamic(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        memo[n] = 1
    else:
        memo[n] = fib_dynamic(n - 1, memo) + fib_dynamic(n - 2, memo)
    return memo[n]


print(fib_dynamic(50))
