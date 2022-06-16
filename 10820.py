import sys

for line in sys.stdin:
    count = [0, 0, 0, 0]
    for l in line:
        if l==" ":
            count[3] += 1
        elif ord('a') <= ord(l) <= ord('z'):
            count[0] += 1
        elif ord('A') <= ord(l) <= ord('Z'):
            count[1] += 1
        elif ord('0') <= ord(l) <= ord('9'):
            count[2] += 1
    print(" ".join(map(str, count)))