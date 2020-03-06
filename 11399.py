n = int(input())
p = list(map(int, input().split()))

p.sort()
time = 0

for i in range(n):
    time += p[i] * (n-i)

print(time)
