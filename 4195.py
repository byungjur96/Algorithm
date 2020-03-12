import sys


def get_parent(x):
    if graph[x] == x:
        return x
    return get_parent(graph[x])


case = int(sys.stdin.readline().rstrip())

for _ in range(case):
    human = 0
    num = int(sys.stdin.readline().rstrip())
    names = []
    root = []
    for _ in range(num):
        a, b = sys.stdin.readline().rstrip().split()
        if a in names:
            a_node = names.index(a)
        else:
            names.append(a)
            root.append(human)
            a_node = human
            human += 1
        if b in names:
            b_node = names.index(b)
        else:
            names.append(b)
            root.append(human)
            b_node = human
            human += 1

        while a_node != root[a_node]:
            a_node = root[a_node]
        while b_node != root[b_node]:
            b_node = root[b_node]

        if a_node < b_node:
            for i in range(human):
                if root[i] == b_node:
                    root[i] = a_node
        elif a_node > b_node:
            for i in range(human):
                if root[i] == a_node:
                    root[i] = b_node

        count = 0
        for i in range(human):
            if root[i] == a_node or root[i] == b_node:
                count += 1
        print(count)
