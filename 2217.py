import sys

n = int(input())
maximum = 0
ropes = []

for _ in range(n):
    ropes.append(int(sys.stdin.readline().rstrip()))

ropes.sort(reverse=True)

for r in range(n):
    val = (r + 1) * ropes[r]
    if val > maximum:
        maximum = val

print(maximum)
