q = [0, 0, 0, 0, 0] # q[0]가 axis

test_case = int(input())
for _ in range(test_case):
    a, b = map(int, input().split())
    if a > 0:
        if b > 0:
            q[1] += 1
        elif b < 0:
            q[4] += 1
        else:
            q[0] += 1
    elif a < 0:
        if b > 0:
            q[2] += 1
        elif b < 0:
            q[3] += 1
        else:
            q[0] += 1
    else:
        q[0] += 1

print("Q1: " + str(q[1]))
print("Q2: " + str(q[2]))
print("Q3: " + str(q[3]))
print("Q4: " + str(q[4]))
print("AXIS: " + str(q[0]))
