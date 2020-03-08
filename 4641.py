import sys


while True:
    total = 0
    line = sys.stdin.readline().rstrip()
    if line == "-1":
        sys.exit()

    lst = list(map(int, line.split()))
    del lst[-1]

    length = len(lst)
    for i in range(length - 1):
        for j in range(i+1, length):
            if lst[i]*2 == lst[j] or lst[i] == lst[j] * 2:
                total += 1
    print(total)
