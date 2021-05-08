string = 'abcd'
#substring in continous fashion
substrings = [string[i:j] for i in range(len(string)) for j in range(i+1,len(string)+1)]
                                                                                  # +1 because slicing excludes last index
print(substrings)

#powerset

list = [1,2,3]

power = []

for i in list:
    power += [i + num for num in list]


print(power)