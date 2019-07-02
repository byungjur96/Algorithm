a = -1
b = -1
while (a != 0) or (b != 0):
    a, b = map(int, input().split(' '))
    if a > b:
        print('Yes')
    else:
        if a != 0 or b != 0:
            print('No')
