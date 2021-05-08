def canSum(arr,total):
    if total == 0:
        return True

    for v in arr:
        subtotal = total - v
        arr.remove(v)
        if canSum(arr,subtotal):
            return True

    return False

def canSum_dp(arr,total,n):
    if total == 0:
        return True
    if total < 0: return False

    if n < 0: return False

    return canSum_dp(arr,total-arr[n],n-1) or canSum_dp(arr,total,n-1)


if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        value = int(input())
        arr.append(value)
    total = int(input())
    print(canSum_dp(arr,total,len(arr)-1))