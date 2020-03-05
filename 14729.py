import sys

n = int(input())
seven = []

for i in range(n):
    score = float(sys.stdin.readline().rstrip())
    if i < 6:
        seven.append(score)
    elif i == 6:
        seven.append(score)
        seven.sort()
    else:
        for j in range(7):
            if seven[j] > score:
                seven.insert(j, score)
                seven.pop()
                break

for s in seven:
    print('%.3f' % s)
