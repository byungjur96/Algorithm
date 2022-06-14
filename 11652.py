import sys

n = int(sys.stdin.readline())
cards = {}
count = 0
val = 0
for _ in range(n):
    c = int(sys.stdin.readline())
    if c in cards:
        cards[c] += 1
    else:
        cards[c] = 1
    if cards[c] > count:
        count = cards[c]
        val = c
    elif cards[c] == count:
        val = min(val, c)
print(val)