import sys
i = sys.stdin.readline

left = list(i().rstrip())
right = []
for _ in range(int(i())):
    c = i().split()
    if c[0] == "P":
        left.append(c[1])
    elif c[0] == "L" and left:
        right.append(left.pop())
    elif c[0] == "D" and right:
        left.append(right.pop())
    elif c[0] == "B" and left:
        left.pop()

print("".join(left) + "".join(right[::-1]))