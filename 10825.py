import sys

n = int(sys.stdin.readline())
score = []

for _ in range(n):
    s = sys.stdin.readline().split()
    score.append([s[0], int(s[1]), int(s[2]), int(s[3])])

score.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))

for s in score:
    print(s[0])