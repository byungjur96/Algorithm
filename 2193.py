result = [1, 1, 1, 2]

num = int(input())

for i in range(4, num+1):
    value = 0
    for j in range(i-1):
        value += result[j]
    result.append(value)

print(result)
