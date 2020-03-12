import sys


def get_parent(x):
    if graph[x] == x:
        return x
    return get_parent(graph[x])


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

connected = []
graph = [i for i in range(n+1)]

# 연결 여부 matrix
for _ in range(n):
    connected.append(list(map(int, sys.stdin.readline().rstrip().split())))

# matrix를 기반으로 graph 작성
for i in range(n):
    for j in range(i+1, n):
        # 연결되어 있다면 joint
        if connected[i][j] == 1:
            a = get_parent(i+1)
            b = get_parent(j+1)
            graph[max(a, b)] = min(a, b)

# 여행 계획 순서
plan = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(m-1):
    departure = plan[i]
    destination = plan[i+1]
    if get_parent(departure) != get_parent(destination):
        print("NO")
        sys.exit()
print("YES")
