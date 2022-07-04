import sys
from collections import deque

def is_bipatite(e,v):
    group = [0 for _ in range(v+1)]
    for i in range(v):
        if group[i+1] != 0:
            continue
        group[i+1] = 1
        edges = deque()
        for edge in e[i+1]:
            edges.append([i+1, edge])
        while edges:
            edge = edges.popleft()
            if group[edge[0]] * group[edge[1]] == 1:
                return "NO"
            for k in e[edge[1]]:
                if group[k] == 0:
                    edges.append([edge[1], k])
            if group[edge[1]] == 0:
                group[edge[1]] = (-1) * group[edge[0]]
            
    return "YES"

result = []
for _ in range(int(sys.stdin.readline())):
    v, e = map(int, sys.stdin.readline().split())
    edges = dict()
    for i in range(v):
        edges[i+1] = []
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        edges[a].append(b)
        edges[b].append(a)
    result.append(is_bipatite(edges, v))
for r in result:
    print(r)