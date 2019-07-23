# a가 무조건 b보다 크다
def gcd(a, b):
    while b > 0:
        temp = a - b
        if temp > b:
            a = temp
        else:
            a = b
            b = temp
    return a


x1, x2 = map(int, input().split())

if x1 > x2:
    cd = gcd(x1, x2)
    print(cd)
    print(int(x1/cd)*x2)
elif x1 < x2:
    cd = gcd(x2, x1)
    print(cd)
    print(int(x1 / cd) * x2)
else:
    print(x1)
    print(x1)
