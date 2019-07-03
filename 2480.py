count = [0, 0, 0, 0, 0, 0]
value = list(map(int, input().split()))

if value[0] == value[1]:
    if value[1] == value[2]:
        print(10000+1000*(value[0]))
    else:
        print(1000 + 100 * (value[0]))

elif value[0] > value[1]:
    if value[2] > value[0]:
        print(value[2] * 100)
    elif value[2] == value[0]:
        print(1000 + 100 * value[0])
    elif value[2] == value[1]:
        print(1000 + 100 * value[1])
    else:
        print(value[0] * 100)

else:
    if value[2] > value[1]:
        print(value[2] * 100)
    elif value[2] == value[0]:
        print(1000 + 100 * value[0])
    elif value[2] == value[1]:
        print(1000 + 100 * value[1])
    else:
        print(value[1] * 100)
