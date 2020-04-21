import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
numbers = []

result = 0

tetrominoes = [
    # 긴거
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    # 네모난거
    [[0, 0], [0, 1], [1, 0], [1, 1]],
    # ㄴ 모양
    [[0, 0], [0, 1], [0, 2], [1, 0]],
    [[0, 2], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 1], [1, 1], [2, 1], [2, 0]],
    [[0, 0], [0, 1], [1, 0], [2, 0]],
    [[0, 0], [0, 1], [1, 1], [2, 1]],
    # 번개 모양
    [[0, 1], [1, 0], [1, 1], [2, 0]],
    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[1, 0], [1, 1], [0, 1], [0, 2]],
    [[0, 0], [0, 1], [1, 1], [1, 2]],
    # ㅗ 모양
    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 0], [1, 0], [2, 0], [1, 1]],
    [[1, 0], [1, 1], [1, 2], [0, 1]],
    [[1, 0], [0, 1], [1, 1], [2, 1]]
]

# 종이 숫자 채우기
for _ in range(n):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    numbers.append(line)

for y in range(n):
    for x in range(m):
        # start_point = [y, x]
        for tetromino in tetrominoes:
            is_possible = True
            # 블록이 종이 안에 들어오는 지 확인하기
            for i in range(4):
                if not (0 <= (y + tetromino[i][0]) < n and 0 <= (x + tetromino[i][1]) < m):
                    is_possible = False
                    break
            # 블록이 종이 안에 들어오면 값 계산하기
            if is_possible:
                temp = 0
                for i in range(4):
                    temp += numbers[y + tetromino[i][0]][x + tetromino[i][1]]
                result = max(temp, result)

print(result)
