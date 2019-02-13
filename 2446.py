n = int(input())

for i in range(n-1):
    for s in range(i):
        print(" ", end="")

    for t in range(2*(n-i-1)+1):
        print("*", end="")
    print()

for i in range(n-1):
    print(" ", end="")

print("*", end="")

for i in range(n-1):
    print()
    for s in range(n-i-2):
        print(" ", end="")

    for t in range(2*(i+1)+1):
        print("*", end="")
