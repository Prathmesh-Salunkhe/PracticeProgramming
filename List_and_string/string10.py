string = input()

dic = dict.fromkeys(string)
print(dic)

for key in dic.keys():
    dic[key] = 0

for ch in string:
    dic[ch] +=1

print(dic)
count =0
for key in dic.keys():
    if dic[key] == 1:
        count +=1

print(count)

