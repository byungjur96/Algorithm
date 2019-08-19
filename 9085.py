test = int(input())
for _ in range(test):
    n = int(input())
    val = list(map(int, input().split()))
    total = 0
    for i in range(n):
        total += val[i]
    print(total)
