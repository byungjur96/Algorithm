def is_vps(string):
    pos = 0

    if len(string) % 2 == 1:
        return False

    else:
        for i in range(len(string)):
            if string[i] == '(':
                pos += 1
            # if ps[i] == ')'
            else:
                pos -= 1
                if pos < 0:
                    return False
        if pos == 0:
            return True
        else:
            return False


line = int(input())

for _ in range(line):
    ps = input()
    if is_vps(ps) is True:
        print('YES')
    else:
        print('NO')
