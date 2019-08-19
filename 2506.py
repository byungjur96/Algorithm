total = 0
point = 0
n = int(input())
result = list(map(int, input().split()))
for i in range(n):
    if result[i] == 1:
        point += 1
        total += point
    elif result[i] == 0:
        point = 0
print(total)
