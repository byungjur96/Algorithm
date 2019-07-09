SWITCHES = 10
CLOCKS = 16
MAX = 4**10 + 1

linked = [
    'xxx.............',
    '...x...x.x.x....',
    '....x.....x...xx',
    'x...xxxx........',
    '......xxx.x.x...',
    'x.x...........xx',
    '...x..........xx',
    '....xx.x......xx',
    '.xxxxx..........',
    '...xxx...x...x..'
]


def check_twelve(h):
    for i in h:
        if i % 12 != 0:
            return False
    return True


def push_btn(h, btn):
    for i in range(CLOCKS):
        if linked[btn][i] == 'x':
            h[i] += 3
            if h[i] == 15:
                h[i] = 3
    return h


def solve(h, btn):
    result = MAX
    if btn == SWITCHES:
        if check_twelve(h):
            return 0
        return result

    for i in range(4):
        result = min(result, i + solve(h, btn + 1))
        h = push_btn(h, btn)
    return result


test_case = int(input())
for _ in range(test_case):
    hours = list(map(int, input().split()))
    print(solve(hours, 0))
