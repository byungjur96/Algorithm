t = int(input())
btn = [0, 0, 0]
btn[0] = t//300
t %= 300
btn[1] = t//60
t %= 60
btn[2] = t//10
t %= 10
if t != 0:
    print('-1')
else:
    print('{0} {1} {2}'.format(btn[0], btn[1], btn[2]))
