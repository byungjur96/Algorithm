n = int(input())
for i in range(n):
    for _ in range(i+1):
        print('*', end="")
    for _ in range(2*n-2*i-2):
        print(' ', end="")
    for _ in range(i + 1):
        print('*', end="")
    print()
for i in range(n-1, 0, -1):
    for _ in range(i):
        print('*', end="")
    for _ in range(2*(n-i)):
        print(' ', end="")
    for _ in range(i):
        print('*', end="")
    print()
