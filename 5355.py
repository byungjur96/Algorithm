test_case = int(input())


def mars_cal():
    line = input().split()
    val = float(line[0])
    for i in range(1, len(line)):
        if line[i] == '@':
            val *= 3
        elif line[i] == '%':
            val += 5
        elif line[i] == '#':
            val -= 7
        else:
            continue
    print(format(val, ".2f"))


for _ in range(test_case):
    mars_cal()
