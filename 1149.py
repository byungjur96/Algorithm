import sys

n = int(input())
minimum_price = 1000 * n
price = []  # 각 집의 칠하는 비용
calculated_cost = [[minimum_price for _ in range(3)] for _ in range(n)]  # i 번까지 칠 비용

for _ in range(n):
    price.append(list(map(int, sys.stdin.readline().rstrip().split())))

calculated_cost[0] = price[0]

for i in range(1, n):
    # 이번에 선택할 색깔
    for color in range(3):
        before = calculated_cost[i - 1]
        if color == 0:
            calculated_cost[i][0] = min(calculated_cost[i][0], min(before[1], before[2])+price[i][0])
        elif color == 1:
            calculated_cost[i][1] = min(calculated_cost[i][1], min(before[0], before[2])+price[i][1])
        else:
            calculated_cost[i][2] = min(calculated_cost[i][2], min(before[0], before[1])+price[i][2])

print(min(calculated_cost[n-1]))
