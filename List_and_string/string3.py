seq = input()
num = ''
for ch in seq: # to get only digits
    if ch.isdigit():
        num += ch

found = False
for ch in num:
    num_list = list(dict.fromkeys(map(int, [ch for ch in num])))
    num_list.sort(reverse=True)
#str.remove(ch) removes a charecter from string an str.insert(index,ch) add ch at index
def make_even(num_list, index):
    for i in range(index, len(num_list) - 1):
        temp = num_list[i]
        num_list[i] = num_list[i + 1]
        num_list[i + 1] = temp
    return num_list

for i in range(len(num_list) - 1, 0,-1):
    if num_list[i] % 2 == 0:
        found = True
        num_list = make_even(num_list, i)
        break

final = ''
for ch in num_list: # to combine the numbers inside a int list
    final +=str(ch)
if found:
    print(final)
else:
    print(-1)
