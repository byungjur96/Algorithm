import sys

computer = int(input())
pairs = int(input())
network = [[0 for _ in range(computer)] for _ in range(computer)]
total = 0

for _ in range(pairs):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    network[x - 1][y - 1] = 1
    network[y - 1][x - 1] = 1

infected = [1]
stack = [1]
while stack:
    val = stack[-1]
    adj = []
    for i in range(computer):
        if network[val-1][i] == 1 and (i+1) not in infected:
            adj.append(i+1)
    if not adj:
        del stack[-1]
    else:
        stack.append(adj[0])
        infected.append((adj[0]))
        total += 1

print(total)
