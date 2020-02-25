case = int(input())

for _ in range(case):
    count = 0
    n, m = map(int, input().split())
    for i in range(n, m+1):
        int_to_str = str(i)
        for s in int_to_str:
            if s == '0':
                count += 1
    print(count)
