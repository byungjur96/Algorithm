x, y = input().split()
minimum = 50

for i in range(len(y) - len(x) + 1):
    temp = 0
    for j in range(len(x)):
        if x[j] != y[i + j]:
            temp += 1
    if temp < minimum:
        minimum = temp

print(minimum)
