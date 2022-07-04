import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    root = [i+1 for i in range(n)]
    net = dict()
    for i in range(n):
        net[i+1] = [i+1]
    e = []
    for idx, l in enumerate(lst):
        if root[idx] > root[l-1]:
            temp = root[idx]
            for n in net[temp]:
                net[root[l-1]].append(n)
                root[n-1] = root[l-1]
            del net[temp]
            root[idx] = root[l-1]
        elif root[idx] < root[l-1]:
            temp = root[l-1]
            for n in net[temp]:
                net[root[idx]].append(n)
                root[n-1] = root[idx]
            del net[temp]
            root[l-1] = root[idx]
    print(len(net))