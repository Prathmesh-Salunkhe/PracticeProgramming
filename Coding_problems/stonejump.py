def stoneJumpCount(n,x,y,z,k):
    count = 0
    if x>=y:
       return 0

    if x < 1:
       return 0

    if k <= 0:
       return 1

    for i in range(1,z+1):
        count += stoneJumpCount(n,x+i,y,z,k-1) + stoneJumpCount(n,x-i,y,z,k-1)

    return count


if __name__ == '__main__':
    n = int(input())        #no of stones
    x = int(input())        #current stone
    y = int(input())        #special stone
    z = int(input())        #jump power
    k = int(input())        #no of jumps

    jumps = stoneJumpCount(n,x,y,z,k)
    print(jumps)