def beautifulFunction(num):
    beautiful_number = num + 1
    while True:
        if beautiful_number %10 != 0:
            break
        beautiful_number /= 10

    return int(beautiful_number)

def beautifulFunctionCount(num,count=1,visited=[]):
    if num < 10:
        return 9
    if num in visited:
        return count

    visited.append(num)

    num = beautifulFunction(num)
    count += beautifulFunctionCount(num,count,visited)

    return count
#
# def beautifulFunctionCount(num):
#     count = 0
#     num = str(num)
#
#     while len(num) > 1:
#         current_count = 10 - int(num[-1])
#         count += current_count
#
#         num = str(beautifulFunction(int(num)))
#         print(num,count)
#
#     count += 9
#
#     return count


if __name__ == '__main__':
    num = int(input())
    count = beautifulFunctionCount(num)
    print(count)