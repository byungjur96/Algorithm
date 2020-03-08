import sys
n = int(input())

meeting = []
max_profit = 0


def plan(day, profit):
    global max_profit
    if day >= n:
        if profit > max_profit:
            max_profit = profit
        return
    # day에 미팅을 안하는 경우
    plan(day+1, profit)
    # day에 미팅을 하는 경우
    if day + meeting[day][0] <= n:
        plan(day + meeting[day][0], profit + meeting[day][1])


for i in range(n):
    meeting.append(list(map(int, sys.stdin.readline().rstrip().split())))

plan(0, 0)

print(max_profit)
