import sys
from collections import deque

def find_farthest(i, v, mat):
    q = deque()
    q.append([i, 0])
    visited = [False for _ in range(v)]
    temp = [0 for _ in range(v)]
    while q:
        val = q.popleft()
        if temp[val[0]] < val[1]:
            temp[val[0]] = val[1]
        visited[val[0]] = True
        for k in mat[val[0]+1]:
            if not visited[k-1]:
                q.append([k-1, val[1]+mat[val[0]+1][k]])
    return [max(temp), temp.index(max(temp))]

n = int(sys.stdin.readline())
length = [0 for _ in range(n)]
matrix = dict()
for i in range(n):
    matrix[i+1] = dict()
result = 0
for i in range(n-1):
    start, end, weight = map(int, sys.stdin.readline().split())
    matrix[start][end] = weight
    matrix[end][start] = weight
start = find_farthest(0, n, matrix)[1]
print(find_farthest(start, n, matrix)[0])
