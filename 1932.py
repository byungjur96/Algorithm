import sys

triangle = []
maximum = []

# 삼각형 만들기
n = int(input())
for i in range(n):
    triangle.append(list(map(int, sys.stdin.readline().rstrip().split())))
    maximum.append([0 for _ in range(i+1)])

maximum[0] = triangle[0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            maximum[i][j] = maximum[i-1][j] + triangle[i][j]
        elif j == i:
            maximum[i][j] = maximum[i - 1][j-1] + triangle[i][j]
        else:
            maximum[i][j] = max(maximum[i - 1][j], maximum[i - 1][j - 1]) + triangle[i][j]

print(max(maximum[n - 1]))
