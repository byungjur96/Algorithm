import math

n = int(input())
a = input().split(" ")
b, c = input().split(" ")

b = int(b)
c = int(c)

total = n

for i in range(n):
    v = int(a[i]) - b
    if v > 0:
        total += math.ceil(v/c)

print(total)
