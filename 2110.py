import sys

n, c = map(int, sys.stdin.readline().rstrip().split())
xi = []
for _ in range(n):
    xi.append(int(sys.stdin.readline().rstrip()))


def router_count(dis):
    total = 1
    pos = xi[0]
    for i in range(1, n):
        if xi[i] - pos >= dis:
            total += 1
            pos = xi[i]
    return total


xi.sort()

start = 1
end = xi[n - 1] - xi[0]


while start <= end:
    gap = (start + end) // 2
    # 개수가 충분히 안나왔을 때 -> 간격을 줄인다
    if router_count(gap) < c:
        end = gap - 1
    else:
        answer = gap
        start = gap + 1

print(answer)
