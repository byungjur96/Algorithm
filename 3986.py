case = int(input())

total = 0
for _ in range(case):
    line = input()
    a_open = False
    b_open = False
    stack = []
    pos = -1
    for l in line:
        if pos == -1:
            stack.append(l)
            pos += 1
        else:
            if stack[pos] == l:
                stack.pop()
                pos -= 1
            else:
                stack.append(l)
                pos += 1
    if len(stack) == 0:
        total += 1
print(total)
