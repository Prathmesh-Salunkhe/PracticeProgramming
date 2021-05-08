num = input()
oddnum=''
for i in range(len(num)):
    if i %2 != 0:
        oddnum += num[i]

#alternative to get odd index
oddnum=''
for i in range(1,len(num),2):       #skips one index
    oddnum += num[i]

print(oddnum)

sqnum=""

for i in oddnum:
    sqnum += str(int(i)**2)

print(sqnum[:4])

