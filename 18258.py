import sys

queue = []
head = -1  # 첫 값 위치
tail = 0  # 다음에 들어올 위치
length = 0


def push(n):
    global head
    global tail
    global length
    if length == 0:
        head += 1
    length += 1
    queue.append(n)
    tail += 1


def pop():
    global head
    global length
    if length == 0:
        return -1
    elif length == 1:
        length -= 1
        return queue[head]
    else:
        head += 1
        length -= 1
        return queue[head - 1]


def empty():
    if length == 0:
        return 1
    else:
        return 0


def front():
    if length == 0:
        return -1
    else:
        return queue[head]


def back():
    if length == 0:
        return -1
    else:
        return queue[tail - 1]


num = int(sys.stdin.readline().rstrip())


for _ in range(num):
    order = sys.stdin.readline().rstrip()
    if order == "pop":
        print(pop())
    elif order == "size":
        print(length)
    elif order == "empty":
        print(empty())
    elif order == "front":
        print(front())
    elif order == "back":
        print(back())
    else:
        push(order.split()[1])
