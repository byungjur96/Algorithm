import sys

triangle = [1, 1, 1, 2, 2, 3, 4]

case = int(input())
for _ in range(case):
    n = int(sys.stdin.readline().rstrip())
    if len(triangle) >= n:
        print(triangle[n-1])
    else:
        for i in range(len(triangle), n):
            triangle.append(triangle[i - 1] + triangle[i - 5])
        print(triangle[n - 1])
