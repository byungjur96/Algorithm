line = int(input())

for i in range(line):
    for _ in range(line-i-1):
        print(" ", end="")
    for _ in range(2*i+1):
        print('*', end="")
    print()
