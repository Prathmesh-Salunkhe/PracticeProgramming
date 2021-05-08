string = input()
x = input()
num = string.split(' ')

print(num)
count = dict.fromkeys(num)

for x in count.keys():
    count[x] = 0
print(count)
for n in num:
    if n in count.keys():
        count[n] += 1


for i in range(int(x)):
    print(i,count)
    min_repeat = 100
    max_repeat = -1
    if min(count.values()) == 1:
        for k in count.keys():
            if count[k] < min_repeat:
                min_repeat = count[k]
                min_ = x
        print(min_)
        count[min_] -= 1
        if count[min_] == 0:
            count.pop(min_)

    else:
        for k in count.keys():
            if count[k] > max_repeat:
                max_repeat = count[k]
                max_ = x
        print(max_)
        count[max_] -= 1
        if count[max_] == 0:
            count.pop(max_)
final = ''
for x in count.keys():
    for i in range(count[x]):
        final += str(x) +' '

print(final)
print(count)