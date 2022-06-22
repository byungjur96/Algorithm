import sys

neighbors = [[-1,0], [1,0], [0, 1], [0,-1]]

def danji(i, j):
    if checked[i][j]:
        return -1
    if apart[i][j] == '0':
        return -1
    idx = 0
    checked[i][j] = True
    q = [[i, j]]
    while len(q) > idx:
        target = q[idx]
        for neighbor in neighbors:
            x = target[0] + neighbor[0]
            y = target[1] + neighbor[1]
            if (0<=x<n) and (0<=y<n) and (checked[x][y]==False) and (apart[x][y] == '1'):
                checked[x][y] = True
                q.append([x, y])
        idx += 1
    return len(q)

n = int(sys.stdin.readline())
apart = []
for _ in range(n):
    apart.append(list(sys.stdin.readline().rstrip()))
checked = [[False for _ in range(n)] for _ in range(n)]

result = []
for i in range(n):
    for j in range(n):
        val = danji(i, j)
        if val > 0:
            result.append(val)

print(len(result))
print("\n".join(list(map(str, sorted(result)))))