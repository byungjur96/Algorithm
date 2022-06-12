n = int(input())
a = list(map(int, input().split()))

result = [a[0]]

for i in range(1, n):
    temp = 0
    for j in range(i):
        if a[j] < a[i]:
            temp = max(temp, result[j])
    result.append(temp+a[i])

print(max(result))