import sys

n = int(sys.stdin.readline())
wine = [int(sys.stdin.readline()) for _ in range(n)]

if n == 1:
    print(wine[0])
    sys.exit()

eat = [wine[0], wine[0]+wine[1]]
skip = [0, wine[0]]

for i in range(2, n):
    eat.append(max(skip[i-1], skip[i-2]+wine[i-1], eat[i-2]) + wine[i])
    skip.append(max(skip[i-1], eat[i-1]))

print(max(eat[n-1], skip[n-1]))