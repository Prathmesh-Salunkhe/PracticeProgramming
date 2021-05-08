num = int(input())

base = int(input())

# num_base = []
# while num > 0:
#     rem = num % base
#     num_base.append(str(rem))
#     num//=base
#
# num_base.reverse()
# num_base = ''.join(num_base)
# print(num_base)

num_base = ''

while num > 0:
    rem = num % base
    num = num//base
    num_base = num_base + str(rem)

num_base = num_base[::-1]
print(num_base)
