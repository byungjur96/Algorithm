def fast_modulo(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 1:
        return (a * fast_modulo(a, b-1, c)) % c
    else:
        return (fast_modulo(a, b//2, c) ** 2) % c


a, b, c = list(map(int, input().split()))
print(fast_modulo(a, b, c))
