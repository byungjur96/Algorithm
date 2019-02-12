n = int(input())

for i in range(1, n):
    for _ in range(n-i):
        print(" ", end="")

    for _ in range(2*i-1):
        print("*", end="")

    print()

for _ in range(2*n-1):
    print("*", end="")


for i in range(n-1, 0, -1):
    print()
    for _ in range(n - i):
        print(" ", end="")

    for _ in range(2 * i - 1):
        print("*", end="")
