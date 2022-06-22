import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    made = [False for _ in range(n)]
    teammate = [False for _ in range(n)]
    result = 0
    
    for i in range(n):
        if teammate[i] or made[i]:
            continue
        mem = i
        q = []
        while not teammate[mem]:
            teammate[mem] = True
            q.append(mem)
            mem = lst[mem]-1
        if (lst[mem]-1) in q:
            q = q[q.index(mem):]
            for v in q:
                made[v] = True

    print(made.count(False))
