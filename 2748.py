n = int(input())
a = 0
b = 1
val = 0

if n == 0:
    print(0)
elif n <= 2:
    print(1)
else:
    for _ in range(n):
        temp = a + b
        a = b
        b = temp
        val = a
    print(val)
