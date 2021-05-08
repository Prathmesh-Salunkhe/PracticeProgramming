def targetSum(arr,target,n,sum1=0,count = 0):
    if sum1 == target:
        return 1

    if n<0:
        return 0

    count += targetSum(arr,target,n-1,sum1 + arr[n],count) + targetSum(arr,target,n-1,sum1 - arr[n],count)

    return count


if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        value = int(input())
        arr.append(value)
    diff = int(input())
    target =sum(arr)
    print(targetSum(arr,target,len(arr) - 1))