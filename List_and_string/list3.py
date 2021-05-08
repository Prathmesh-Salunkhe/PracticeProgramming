result = [[2,3],[4,5]]
result.append(3)
print(result)

result = [[2,3],[4,5]]
print(result.append(3))

result = [[2,3],[4,5]]
print(result +[3])

result = [[2,3],[4,5]]
for ele in result:
    ele = ele + [3]
print(result)

result = [[2,3],[4,5]]
for i in range(len(result)):
    result[i] = result[i] + [3]
print(result)

result = [[2,3],[4,5]]
numadd = [[6,7]]

print(result + numadd)

print(result.append(numadd))
result = [[2,3],[4,5]]
for i in range(len(result)):
    for j in range(len(numadd)):
        result[i] = result[i] + numadd[j]

print(result)


