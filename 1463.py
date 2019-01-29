result = [0]
number = int(input())

for i in range(2, number + 1):
    minimum = result[i - 2]

    if i % 3 == 0:
        if result[int(i/3)-1] < minimum:
            minimum = result[int(i/3)-1]

    if i % 2 == 0:
        if result[int(i/2)-1] < minimum:
            minimum = result[int(i/2)-1]

    result.append(minimum + 1)

print(result[number - 1])
