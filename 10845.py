import sys

queue = []


def push(n):
    queue.append(n)


def pop():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])
        del queue[0]


def size():
    print(len(queue))


def empty():
    if len(queue) == 0:
        print(1)
    else:
        print(0)


def front():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])


def back():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])


num = int(sys.stdin.readline().rstrip())

for _ in range(num):
    order = sys.stdin.readline().rstrip()

    if order == 'pop':
        pop()
    elif order == 'size':
        size()
    elif order == 'empty':
        empty()
    elif order == 'front':
        front()
    elif order == 'back':
        back()
    else:
        push(order.split(" ")[1])
