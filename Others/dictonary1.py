## to delete 'num' element from list such that there are min number of unique element. print count of non unique elements

num = int(input())

list1 = list(map(int, input().split()))
print(list1)

d = dict.fromkeys(list1)
for key in d.keys():
    d[key] = 0

for i in list:
    d[i] += 1


def min_repeat(d):
    min_value = 1000

    for key in d.keys():
        if d[key] < min_value:
            min_key = key
            min_value = d[key]

    return min_key

print(d)
for i in range(num):
    min = min_repeat(d)
    if d[min] == 1:
        del d[min]

    else:
        d[min] -=1

print(d)

count = 0
for key in d.keys():
    if d[key] > 1 :
        count +=1

print(count)