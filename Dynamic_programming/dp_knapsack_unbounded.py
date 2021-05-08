def knapsackUnbounded(weight,profit,capacity,n):
    if n<0:
        return 0
    if weight[n] > capacity:
        return knapsackUnbounded(weight,profit,capacity,n-1)

    return max(profit[n] +knapsackUnbounded(weight,profit,capacity-weight[n],n) , knapsackUnbounded(weight,profit,capacity,n-1))


if __name__ == "__main__":
    n = int(input())
    weight = []
    profit = []
    for i in range(n):
        wt,pt = map(int,input().split())
        weight.append(wt)
        profit.append(pt)

    capacity = int(input())

    print(knapsackUnbounded(weight,profit,capacity,len(weight)-1))