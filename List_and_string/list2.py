
key = input()
str_num = str(key)
list_num = []
count =  0
for digit in str_num:
    list_num.append(digit)
    if digit == '0':
        count +=1
list_num.sort()
print(list_num)

for i in range(count):
    if '0' in list_num:
        list_num.remove('0')

for i in range(count):
    list_num.insert(1,'0')

str_num= ''.join(list_num)

num = int(str_num)


print(num)
