case = int(input())
for _ in range(case):
    p, m = map(int, input().split())
    participate = [0 for i in range(m)]
    for i in range(p):
        participate[int(input())-1] += 1

    total = 0

    for i in range(m):
        if participate[i] != 0:
            total += (participate[i] - 1)

    print(total)
