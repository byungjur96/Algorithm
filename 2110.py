import sys

n, c = map(int, sys.stdin.readline().split())
house = []
for i in range(n):
    house.append(int(sys.stdin.readline()))
house.sort()
low = 0
high = (house[-1] // (c - 1)) + 1

while low + 1 < high:
    idx = 0
    cur = 0
    count = 1
    mid = (low + high) // 2
    while idx < n:
        if house[idx] - house[cur] >= mid:
            count += 1
            cur = idx
        idx += 1
    if count < c:
        high = mid
    else:
        low = mid

print(low)