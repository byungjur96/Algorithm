n = int(input())
budgets = list(map(int, input().split()))
M = int(input())

low = 1
high = max(budgets)
mid = (low + high) // 2
while True:
    mid = (low + high) // 2
    if low > high:
        break
    temp = M
    for budget in budgets:
        temp -= min(mid, budget)
    # 상한액이 줄어야 하는 경우
    if temp < 0:
        high = mid - 1
    # 상한액이 늘어야 하는 경우
    else:
        low = mid + 1

print(mid)
