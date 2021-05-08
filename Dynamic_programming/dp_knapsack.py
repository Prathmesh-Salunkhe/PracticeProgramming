def knapsack(weight,value,capacity,n,memo = {}):
    if n == 0 or w == 0:
        return 0
    if (capacity,n) in memo:
        return memo[(capacity,n)]
    if weight[n]>capacity:
        return knapsack(weight,value,capacity,n-1)

    memo[(capacity,n)] = max( value[n] + knapsack(weight,value,capacity-weight[n],n-1),knapsack(weight,value,capacity,n-1))
    return memo[(capacity,n)]


if __name__ == '__main__':
    n = int(input())
    weight = []
    value = []
    for i in range(n):
        w,v = map(int,input().split())
        weight.append(w)
        value.append(v)

    capacity = int(input())

    profit = knapsack(weight,value,capacity,n-1)
    print(profit)



#Sample input
# 4
# 2 100
# 3 400
# 5 300
# 1 100
# 8