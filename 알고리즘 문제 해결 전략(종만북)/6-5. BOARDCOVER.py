cover_type = [
    [[0, 0], [1, 0], [0, 1]],
    [[0, 0], [0, 1], [1, 1]],
    [[0, 0], [1, 0], [1, 1]],
    [[0, 0], [1, 0], [1, -1]]
]
board = []


def set_block(x, y, style, delta):
    ok = True
    # 블록을 판에 놓는다
    if delta is True:

        for i in range(3):
            temp_x = x + cover_type[style][i][0]
            temp_y = y + cover_type[style][i][1]
            if temp_x >= h or temp_y >= w or board[temp_x][temp_y] is False:
                ok = False
        if ok is True:
            for i in range(3):
                temp_x = x + cover_type[style][i][0]
                temp_y = y + cover_type[style][i][1]
                board[temp_x][temp_y] = False
        return ok
    # 블록을 판에서 치운다
    else:
        for i in range(3):
            temp_x = x + cover_type[style][i][0]
            temp_y = y + cover_type[style][i][1]
            board[temp_x][temp_y] = True
        return True


def cover():
    # 시작점을 찾는다
    x = -1
    y = -1
    for sx in range(h):
        for sy in range(w):
            if board[sx][sy] is True:
                x = sx
                y = sy
                break
        if y != -1:
            break

    if y == -1:
        return 1

    ret = 0
    for i in range(4):
        if set_block(x, y, i, True):
            ret += cover()
            set_block(x, y, i, False)

    return ret


test_case = int(input())
for _ in range(test_case):
    h, w = map(int, input().split())
    board = []
    # 보드 모양을 만든다
    for i in range(h):
        board.append([])
        line = input()
        for c in line:
            if c == '#':
                board[i].append(False)
            else:
                board[i].append(True)
    print(cover())
