woman, man, intern = map(int, input().split())
team = 0

while (woman + man >= intern + 3) and woman >= 2 and man >= 1:
    woman -= 2
    man -= 1
    team += 1

print(team)
