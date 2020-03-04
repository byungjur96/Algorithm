import sys

stack = []
total = 0


def push(n):
    stack.append(n)


def pop():
    if total == 0:
        print(-1)
    else:
        print(stack[total - 1])
        del stack[total - 1]


def size():
    print(total)


def empty():
    if total == 0:
        print(1)
    else:
        print(0)


def top():
    if total == 0:
        print(-1)
    else:
        print(stack[total-1])


num = int(sys.stdin.readline().rstrip())

for _ in range(num):
    order = sys.stdin.readline().rstrip()

    if order == 'pop':
        pop()
        if total != 0:
            total -= 1
    elif order == 'size':
        size()
    elif order == 'empty':
        empty()
    elif order == 'top':
        top()
    else:
        total += 1
        push(int(order.split()[1]))
