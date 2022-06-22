import sys
arounds =  [[0, 1], [0, -1], [1, 0], [-1, 0]]

m, n = map(int, sys.stdin.readline().split())
IMPOSSIBLE = m * n + 1

tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
done = [[IMPOSSIBLE for _ in range(m)] for _ in range(n)]
q = []

for i in range(m):
    for j in range(n):
        if tomato[j][i] == 1:
            q.append([i, j])
            done[j][i] = 0
        elif tomato[j][i] == -1:
            done[j][i] = 0
idx = 0
while len(q) > idx:
    t = q[idx]
    for a in arounds:
        x = t[0] + a[0]
        y = t[1] + a[1]
        if 0<=x<m and 0<=y<n and tomato[y][x] == 0:
            tomato[y][x] = 1
            if done[y][x] > done[t[1]][t[0]] + 1:
                done[y][x] = done[t[1]][t[0]] + 1
                q.append([x, y])
    idx+=1

print((max([max(done[i]) for i in range(n)])+1)%(IMPOSSIBLE+1)-1)