#num = int(input())
#'55674'
#string = input()

#list_num = list(map(int, input().split(' ')))
#print(list_num)

#str = '43434'
#list1 = []
#for ch in str:
#    num = int(ch)
#    list1.append(num)

#print(list1)

#string = '01235'
#print(string)

list1 = [1,2,3,4,2,7,3]

#unique = set(list1)
#tu = tuple(list1)
#print(tu)

d = dict.fromkeys(list1)
print(d)

for key in d.keys():
    d[key] = 0

print(d)
for i in list1:
    d[i] += 1

print(d)

unique = []
for key in d.keys():
    if d[key] == 1:
        unique.append(key)

print(unique)
print(d.values())


