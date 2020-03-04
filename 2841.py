import sys
n, total_p = map(int, sys.stdin.readline().rstrip().split())

lines = [[] for _ in range(6)]
move = 0
for _ in range(n):
    l, p = map(int, sys.stdin.readline().rstrip().split())
    # 아무 프렛도 안 눌려져 있는 경우 그냥 누른다.
    length = len(lines[l - 1])
    if length == 0:
        move += 1
        lines[l-1].append(p)
        length += 1
    else:
        while length > 0 and lines[l-1][length-1] > p:
            lines[l-1].pop()
            move += 1
            length -= 1
        if length == 0 or lines[l-1][-1] != p:
            lines[l-1].append(p)
            move += 1
            length += 1

print(move)

