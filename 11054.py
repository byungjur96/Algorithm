n = int(input())
a = list(map(int, input().split()))
increasing = [1 for _ in range(n)]
decreasing = [1 for _ in range(n)]

for i in range(n):
    # increasing check
    temp_inc = 1
    for j in range(i):
        if a[j] < a[i]:
            temp_inc = max(temp_inc, increasing[j]+1)
    increasing[i] = temp_inc

for i in range(n-1, -1, -1):
    # decreasing check
    temp_dec = 1
    for j in range(n-1, i, -1):
        if a[j] < a[i]:
            temp_dec = max(temp_dec, decreasing[j] + 1)
    decreasing[i] = temp_dec

result = 1
for i in range(n):
    result = max(result, increasing[i] + decreasing[i] - 1)

print(result)
