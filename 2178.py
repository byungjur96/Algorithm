from collections import deque
import sys

def find_distance():
    around = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    n, m = map(int, sys.stdin.readline().split())
    MAXIMUM = n * m + 1
    maze = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
    dis = [[MAXIMUM for _ in range(m)] for _ in range(n)]
    dis[0][0] = 1
    q = deque()
    q.append([0, 0])
    while q:
        t = q.popleft()
        if maze[t[0]][t[1]] == '0':
            continue
        maze[t[0]][t[1]] = '0'
        for a in around:
            x = t[0] + a[0]
            y = t[1] + a[1]
            if 0 <= x < n and 0 <= y < m and maze[x][y] == '1':
                if dis[x][y] > dis[t[0]][t[1]] + 1:
                    dis[x][y] = dis[t[0]][t[1]] + 1
                if x == n-1 and y == m-1:
                    return dis[x][y]
                q.append([x, y])
            
print(find_distance())