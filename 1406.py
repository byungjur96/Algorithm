import sys
i = sys.stdin.readline

left = list(i().rstrip())
right = []
for _ in range(int(i())):
    c = i().split()
    if len(c) == 2:
        left.append(c[1])
    else:
        if c[0] == "L":
            if left:
                right.append(left.pop())
        elif c[0] == "D":
            if right:
                left.append(right.pop())
        elif c[0] == "B":
            if left:
                left.pop()

    # print(left, right)

if left:     
    for i in left:
        print(i, end="")
while right:
    print(right.pop(), end="")
print()