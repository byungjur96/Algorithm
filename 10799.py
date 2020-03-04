line = input()
accumulated = 0
orig = 0
pieces = 0
l = 0
while l < len(line):
    # 레이저인 경우
    if line[l] == "(" and line[l+1] == ")":
        pieces += accumulated
        l += 2
        continue
    elif line[l] == "(":
        accumulated += 1
        orig += 1
    else:
        accumulated -= 1
    l += 1

print(pieces + orig)
