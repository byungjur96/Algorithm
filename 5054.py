case = int(input())

for _ in range(case):
    n = int(input())
    xi = list(map(int, input().split()))
    start = xi[0]
    end = xi[0]
    for i in xi:
        if start > i:
            start = i
        if i > end:
            end = i
    print(2*(end-start))
