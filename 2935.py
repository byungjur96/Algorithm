a = input()
cal = input()
b = input()

if cal == '*':
    print('1', end="")
    for _ in range(len(a)+len(b)-2):
        print('0', end="")
    print()
else:
    print(int(a)+int(b))
