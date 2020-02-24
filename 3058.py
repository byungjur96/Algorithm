case = int(input())

for _ in range(case):
    total = 0
    min_val = 100
    num = list(map(int, input().split()))
    for n in num:
        if n % 2 == 0:
            total += n
            if n < min_val:
                min_val = n
    print(total, min_val)
