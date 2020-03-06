import sys

n, m = map(int, input().split())
minimum = []

for i in range(n):
    p, l = map(int, sys.stdin.readline().rstrip().split())
    mileage = list(map(int, sys.stdin.readline().rstrip().split()))
    if l > p:
        minimum.append(1)
    else:
        mileage.sort(reverse=True)
        minimum.append(mileage[l - 1])
minimum.sort()
possible = 0
for i in range(n):
    if m - minimum[i] >= 0:
        m -= minimum[i]
        possible += 1
print(possible)
