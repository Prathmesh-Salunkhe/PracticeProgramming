str = input()
str_list = str.split(',')
final = ''
for x in str_list:
    name, num = x.split(':')
    num_list = list(map(int, [a for a in num]))
    print(num_list)
    square_num = [a ** 2 for a in num_list]
    print(square_num)
    sum_num = sum(square_num)

    if sum_num % 2 == 0:
        final += name[-2:] + name[:-2]
    else:
        final += name[1:] + name[0]

    final += ' '

print(final)
