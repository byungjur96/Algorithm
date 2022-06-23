import sys
from collections import deque

n = int(sys.stdin.readline())

nodes = dict()
tree = dict()

for i in range(n):
    nodes[i+1] = []
    tree[i+1] = []
vertex = [list(map(int, sys.stdin.readline().split())) for _ in range(n-1)]

for v in vertex:
    nodes[v[0]].append(v[1])
    nodes[v[1]].append(v[0])

q = deque()
q.append(1)
checked = [False for _ in range(n+1)]
parent = [None for _ in range(n-1)]

while q:
    pos = q.popleft()
    if checked[pos]:
        continue
    checked[pos] = True
    children = nodes[pos]
    for child in children:
        if not checked[child]:
            q.append(child)
            tree[pos].append(child)
            parent[child-2] = str(pos)

print("\n".join(parent))