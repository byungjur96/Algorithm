line = int(input())
money = []

for i in range(line):
    val = int(input())
    if val == 0:
        money.pop()
    else:
        money.append(val)
total = 0
for m in money:
    total += m

print(total)
