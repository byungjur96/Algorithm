def one_turn():
    value = list(map(int, input().split()))

    if value[0] == value[1]:
        if value[1] == value[2]:
            return 10000+1000*(value[0])
        else:
            return 1000 + 100 * (value[0])

    elif value[0] > value[1]:
        if value[2] > value[0]:
            return value[2] * 100
        elif value[2] == value[0]:
            return 1000 + 100 * value[0]
        elif value[2] == value[1]:
            return 1000 + 100 * value[1]
        else:
            return value[0] * 100

    else:
        if value[2] > value[1]:
            return value[2] * 100
        elif value[2] == value[0]:
            return 1000 + 100 * value[0]
        elif value[2] == value[1]:
            return 1000 + 100 * value[1]
        else:
            return value[1] * 100


n = int(input())
max_val = 0
for _ in range(n):
    cur_val = one_turn()
    if cur_val > max_val:
        max_val = cur_val

print(max_val)
