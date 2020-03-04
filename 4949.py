import sys

while True:
    line = input()
    if line == ".":
        sys.exit()

    balanced = True
    stack = []
    pos = -1

    for l in line:
        if l == "[":
            stack.append("[")
            pos += 1
        elif l == "(":
            stack.append("(")
            pos += 1
        elif l == "]":
            if pos < 0:
                balanced = False
            elif stack[pos] == "[":
                stack.pop()
                pos -= 1
            else:
                balanced = False
        elif l == ")":
            if pos < 0:
                balanced = False
            elif stack[pos] == "(":
                stack.pop()
                pos -= 1
            else:
                balanced = False
        elif l == ".":
            if pos == -1 and balanced is True:
                print("yes")
            else:
                print("no")
