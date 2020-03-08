import sys

n, m = map(int, input().split())
min_paint = 64

board = []

for i in range(n):

    board.append(sys.stdin.readline().rstrip())

for i in range(n-7):
    for j in range(m-7):
        # 작은 8 * 8로 자르기
        paint = 0
        for x in range(8):
            for y in range(8):
                # 무조건 W로 시작한다고 가정
                if (x+y) % 2 == 0:
                    if board[i+x][j+y] != "W":
                        paint += 1
                else:
                    if board[i + x][j + y] != "B":
                        paint += 1
        if paint > 32:
            paint = 64 - paint
        if min_paint > paint:
            min_paint = paint

print(min_paint)
