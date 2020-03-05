import sys

deque = []
d_size = 0


def push_front(x):
    global d_size
    d_size += 1
    deque.insert(0, x)


def push_back(x):
    global d_size
    d_size += 1
    deque.append(x)


def pop_front():
    global d_size
    if d_size == 0:
        return -1
    val = deque[0]
    del deque[0]
    d_size -= 1
    return val


def pop_back():
    global d_size
    if d_size == 0:
        return -1
    val = deque[d_size - 1]
    del deque[d_size - 1]
    d_size -= 1
    return val


def size():
    return d_size


def empty():
    if d_size == 0:
        return 1
    else:
        return 0


def front():
    if d_size == 0:
        return -1
    else:
        return deque[0]


def back():
    if d_size == 0:
        return -1
    else:
        return deque[d_size - 1]


lines = int(sys.stdin.readline().rstrip())

for _ in range(lines):
    command = sys.stdin.readline().rstrip()
    if len(command.split()) == 2:
        func, param = command.split()
        eval("{}({})".format(func, param))
    else:
        print(eval(command+"()"))
