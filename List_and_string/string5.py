#'asdfa:1623,asjdfhasj:287346,asjdfah:1231'

str = input()
ind = str.split(',')
final = ''
print(ind)
for a in ind:
    name, num = a.split(':')
    print(name, num)
    digits = list(map(int, [x for x in num]))
    digits.sort()
    digits.reverse()
    print(digits)
    max_digit = 11
    for dig in digits:  # to get individual digits
        if dig <= len(name):
            max_digit = dig
            break
    print(max_digit)

    if max_digit > len(name):
        final += 'X'

    else:
        final += name[max_digit - 1]

print(final)
