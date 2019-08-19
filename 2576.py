min_val = -1
total = 0

for _ in range(7):
    val = int(input())
    if val % 2 == 1:
        total += val
        if min_val == -1 or min_val > val:
            min_val = val

if min_val == -1:
    print(-1)
else:
    print(total)
    print(min_val)
