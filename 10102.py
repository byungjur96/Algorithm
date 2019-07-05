v = int(input())
value = 0
vote = input()
for t in vote:
    if t == 'A':
        value += 1
    else:
        value -= 1
if value > 0:
    print('A')
elif value < 0:
    print('B')
else:
    print('Tie')
