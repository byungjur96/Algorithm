import sys

case = int(input())
for _ in range(case):
    possible = True  # Error 체크용

    order = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    array = sys.stdin.readline().rstrip()[1:-1].split(",")

    start = 0
    end = n

    # 함수 하나하나 실행하기.
    for o in order:
        # 뒤집기.
        if o == "R":
            # 왼쪽에서 시작하는 경우.
            if end > start:
                end -= 1
                start -= 1
            # 오른 쪽에서 시작하는 경우.
            elif start > end:
                end += 1
                start += 1
            temp = end
            end = start
            start = temp

        # 버리기.
        if o == "D":
            # 왼쪽에서 시작하는 경우.
            if end > start:
                start += 1
            # 오른쪽에서 시작하는 경우.
            elif start > end:
                start -= 1
            elif start == end:
                possible = False
                break
    if possible:
        print("[", end="")
        if start < end:
            for i in range(start, end-1):
                print(array[i], end=",")
            print(array[end-1], end="")
        elif start > end:
            for i in range(start, end+1, -1):
                print(array[i], end=",")
            print(array[end+1], end="")
        print("]")
    else:
        print("error")
