import sys

k, n = map(int, input().split())
lans = []
result = 0
low = 0
high = 0
mid = (low + high) // 2

for _ in range(k):
    val = int(sys.stdin.readline().rstrip())
    lans.append(val)
    if val > high:
        high = val

num = 1  # 조각의 개수
while low <= high:
    num = 0
    mid = max(1, (low + high) // 2)
    for lan in lans:
        num += lan // mid
    # 조각이 덜 나온 경우 -> 길이를 짧게
    if num < n:
        high = mid - 1
    # 조각이 더 나온 경우 -> 길이를 길게
    else:
        result = max(mid, result)
        low = mid + 1

print(result)
