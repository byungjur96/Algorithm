case = int(input())

for _ in range(case):
    num = int(input())
    pos = []
    cur = 0
    while num > 0:
        if num % 2 == 1:
            pos.append(str(cur))
        num = num // 2
        cur += 1
    print(" ".join(pos))
