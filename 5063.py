test_case = int(input())
for _ in range(test_case):
    r, e, c = map(int, input().split())
    do = e - c
    if r == do:
        print('does not matter')
    elif r > do:
        print("do not advertise")
    else:
        print("advertise")
