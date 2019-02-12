for _ in range(3):
    value = 0
    yut = input().split(' ')
    for y in yut:
        value += int(y)

    if value == 0:
        print('D')
    elif value == 1:
        print('C')
    elif value == 2:
        print('B')
    elif value == 3:
        print('A')
    else:
        print('E')
