import sys

n, m = map(int, sys.stdin.readline().split())
mat = [[False for _ in range(n)] for _ in range(n)]
connected = [False for _ in range(n)]
visited = [False for _ in range(n)]
result = 0

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    mat[u-1][v-1] = True
    mat[v-1][u-1] = True

for i in range(n):
    if connected[i]:
        continue
    
    result += 1
    queue = [i+1]
    while queue:
        target = queue.pop(0)
        for j in range(n):
            if not visited[j] and not connected[j] and mat[target-1][j]:
                queue.append(j+1)
                connected[j] = True
        visited[target-1] = True

print(result)