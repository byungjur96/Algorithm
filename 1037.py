num = int(input())
divisor = list(map(int, input().split()))

min_d = divisor[0]
max_d = divisor[0]

for d in divisor:
    if d < min_d:
        min_d = d
    if d > max_d:
        max_d = d

print(max_d * min_d)
