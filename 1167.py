import sys
from collections import deque

def find_farthest(i, v, mat):
    q = deque()
    q.append([i, 0])
    visited = [False for _ in range(v+1)]
    temp = [0 for _ in range(v+1)]
    while q:
        val = q.popleft()
        if temp[val[0]] < val[1]:
            temp[val[0]] = val[1]
        visited[val[0]] = True
        for k in mat[val[0]]:
            if not visited[k]:
                q.append([k, val[1]+mat[val[0]][k]])
    return [max(temp), temp.index(max(temp))]

v = int(sys.stdin.readline())
length = [0 for _ in range(v)]
matrix = dict()
result = 0
for i in range(v):
    line = list(map(int, sys.stdin.readline().split()))
    val = line[0]
    line = line[1:-1]
    matrix[val] = dict()
    for l in range(len(line) // 2):
        [a, b] = line[2*l : 2*l+2]
        matrix[val][a] = b
start = find_farthest(1, v, matrix)[1]
print(find_farthest(start, v, matrix)[0])

