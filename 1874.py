import sys

n = int(input())
is_possible = True
before = 0
num = 0
stack = []
result = []
operation = []
for _ in range(n):
    val = int(input())
    # 값이 증가한 경우
    if val > before:
        while num < val:
            num += 1
            stack.append(num)
            operation.append("+")
        operation.append("-")
        stack.pop()
    # 값이 감소한 경우
    else:
        if stack[-1] == val:
            stack.pop()
            operation.append("-")
        else:
            is_possible = False
    before = val
if is_possible is False:
    print("NO")
else:
    for o in operation:
        print(o)
