n = int(input())
a = list(map(int, input().split()))
length = [1] * n

for i in range(n):
    for j in range(0, i):
        if a[j] > a[i] and length[j] >= length[i]:
            length[i] = length[j] + 1

print(max(length))