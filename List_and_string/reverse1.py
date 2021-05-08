list1 = [1,2,3,4]

for i in range(len(list1)//2):
    print(i,len(list1)-1-i)
    list1[i],list1[len(list1)-1-i] = list1[len(list1) -1 -i], list1[i]

print(list1)