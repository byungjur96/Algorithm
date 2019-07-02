num = int(input())
d = 2

while num > 1:
    if num % d == 0:
        num = int(num/d)
        print(d)
        d = 2
    else:
        d += 1
