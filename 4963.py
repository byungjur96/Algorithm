import sys

xs = [-1, 0, 1]
ys = [-1, 0, 1]
result = []

def find_island(i, j):
    if board[i][j] == '0':
        return 0
    q = [[i, j]]
    while q:
        target = q.pop(0)
        if board[target[0]][target[1]] == '1':
            board[target[0]][target[1]] = '0'
            for x in xs:
                for y in ys:
                    pos_x = target[1] + x
                    pos_y = target[0] + y
                    if 0<= pos_y <h and 0<= pos_x <w:
                        q.append([pos_y, pos_x])
    return 1

w, h = map(int, sys.stdin.readline().split())
while w != 0 and h != 0:
    island = 0
    board = [list(sys.stdin.readline().split()) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            island += find_island(i, j)
    result.append(str(island))
    w, h = map(int, sys.stdin.readline().split())
    
print("\n".join(result))