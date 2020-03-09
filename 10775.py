import sys

g = int(sys.stdin.readline().rstrip())
p = int(sys.stdin.readline().rstrip())

expected_gate = [i for i in range(g+1)]
count = 0
possible = True

for _ in range(p):
    gi = int(sys.stdin.readline().rstrip())
    # gi가 비어 있는 경우
    if gi == expected_gate[gi]:
        expected_gate[gi] -= 1
        if possible:
            count += 1
    # gi가 차 있는 경우
    else:
        while gi != expected_gate[gi]:
            expected_gate[gi] -= 1
            gi = expected_gate[gi] + 1
        if expected_gate[gi] > 0:
            if possible:
                count += 1
        else:
            possible = False

print(count)
