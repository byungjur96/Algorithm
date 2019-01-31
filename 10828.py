stack = []


def push(n):
    stack.append(n)


def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
        del stack[-1]


def size():
    print(len(stack))


def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)


def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])


num = int(input())

for _ in range(num):
    order = input()

    if order == 'pop':
        pop()
    elif order == 'size':
        size()
    elif order == 'empty':
        empty()
    elif order == 'top':
        top()
    else:
        push(order.split(" ")[1])
