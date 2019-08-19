f0 = 0
f1 = 1

n = int(input())

if n == 0:
    print(0)
elif n == 1 or n == 2:
    print(1)
else:
    for _ in range(n-1):
        temp = f0 + f1
        f0 = f1
        f1 = temp
    print(f1)
