score = []
total = [0, 0, 0, 0, 0]
for i in range(5):
    point = input().split()
    score.append(point)

for i in range(5):
    for j in range(5):
        if j < i:
            total[i] += int(score[i][j])
        elif j == i:
            continue
        else:
            total[i] += int(score[i][j-1])

winner = 0
for i in range(5):
    if total[winner] < total[i]:
        winner = i

print(winner+1, total[winner])
