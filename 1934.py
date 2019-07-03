test = int(input())


def swap(a, b):
    return b, a


def gcd(a, b):
    while b % a != 0:
        a, b = swap(a, b % a)
    return a


def lcm():
    a, b = map(int, input().split())
    if a > b:
        a, b = swap(a, b)
    print(int((a/gcd(a, b))*b))


for _ in range(test):
    lcm()
