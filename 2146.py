import sys
from collections import deque

around = [[1, 0], [-1, 0], [0, 1], [0, -1]]
n = int(sys.stdin.readline())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

islands = dict()
idx = 2

for i in range(n):
    for j in range(n):
        if maps[i][j] != 1:
            continue
        q = deque()
        island = []
        q.append([i, j])
        maps[i][j] == idx
        while q:
            t = q.popleft()
            if maps[t[0]][t[1]] == 0:
                continue
            is_outside = False
            for a in around:
                x = t[0] + a[0]
                y = t[1] + a[1]
                if 0 <= x < n and 0 <= y <n:
                    if maps[x][y] == 0:
                        is_outside = True
                    if maps[x][y] == 1:
                        q.append([x, y])
                        maps[x][y] = idx
            if is_outside:
                island.append([t[0], t[1]])
        islands[idx] = island
        idx+=1

MAXIMUM = n * n + 1
result = MAXIMUM

idxs = list(islands.keys())

for i in range(len(idxs)):
    for j in range(i+1, len(idxs)):
        xs = islands[idxs[i]]
        ys = islands[idxs[j]]
        for x in xs:
            for y in ys:
                result = min(result, abs(x[0]-y[0]) + abs(x[1]-y[1]) - 1)
print(result)
