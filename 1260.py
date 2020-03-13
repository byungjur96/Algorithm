import sys


def dfs(g, start):
    stack = [start]
    order = []
    while stack:
        val = stack[-1]
        if val not in order:
            order.append(val)
        adj = []
        for i in range(n-1, -1, -1):
            if g[val-1][i] == 1 and (i+1) not in order:
                adj.append(i+1)
        if not adj:
            del stack[-1]
        else:
            stack += adj
    result = map(str, order)
    return result


def bfs(g, start):
    queue = [start]
    order = []
    while queue:
        val = queue[0]
        if val not in order:
            order.append(val)
        adj = []
        for i in range(n):
            if g[val-1][i] == 1 and (i+1) not in order and (i+1) not in queue:
                adj.append(i+1)
        if not adj:
            del queue[0]
        else:
            queue += adj
    result = map(str, order)
    return result


n, m, v = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    graph[x - 1][y - 1] = 1
    graph[y - 1][x - 1] = 1

print(" ".join(dfs(graph, v)))
print(" ".join(bfs(graph, v)))
