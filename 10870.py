def next_val(a, b):
    next = a+b
    return b, next

n = int(input())

n0 = 0
n1 = 1

if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for _ in range(n-1):
        n0, n1 = next_val(n0, n1)
    print(n1)
