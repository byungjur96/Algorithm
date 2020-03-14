import sys
import copy


def affection(new_map, virus_locations):
    result = 0
    visited = []
    queue = copy.deepcopy(virus_locations)
    while queue:
        [x, y] = queue[0]
        if [x, y] in visited:
            del queue[0]
            continue

        visited.append([x, y])

        if 0 <= x - 1 < n and new_map[x - 1][y] == "0":
            new_map[x - 1][y] = "2"
            queue.append([x - 1, y])
        if 0 <= x + 1 < n and new_map[x + 1][y] == "0":
            new_map[x + 1][y] = "2"
            queue.append([x + 1, y])
        if 0 <= y + 1 < m and new_map[x][y + 1] == "0":
            new_map[x][y + 1] = "2"
            queue.append([x, y + 1])
        if 0 <= y - 1 < m and new_map[x][y - 1] == "0":
            new_map[x][y - 1] = "2"
            queue.append([x, y - 1])
        del queue[0]

    # 안전 영역을 모두 센다.
    for i in range(n):
        for j in range(m):
            if new_map[i][j] == "0":
                result += 1
    return result


n, m = map(int, input().split())
maps = []
blank = []
virus = []
maximum = 0

# 지도 만들기
for _ in range(n):
    maps.append(list(sys.stdin.readline().rstrip().split()))

# 다음 타겟 찾기
for i in range(n):
    for j in range(m):
        if maps[i][j] == "0":
            blank.append([i, j])
        elif maps[i][j] == "2":
            virus.append([i, j])

blank_num = len(blank)
for x in range(blank_num - 2):
    for y in range(x + 1, blank_num - 1):
        for z in range(y+1, blank_num):
            new_map = copy.deepcopy(maps)

            new_map[blank[x][0]][blank[x][1]] = "1"
            new_map[blank[y][0]][blank[y][1]] = "1"
            new_map[blank[z][0]][blank[z][1]] = "1"

            val = affection(new_map, virus)
            maximum = max(val, maximum)

print(maximum)
