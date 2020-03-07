n = int(input())
rings = list(map(int, input().split()))


def gcd(a, b):
    while a != b:
        temp1 = b
        temp2 = a - b
        if temp1 > temp2:
            a = temp1
            b = temp2
        else:
            a = temp2
            b = temp1
    return b


first = rings[0]
rings = rings[1:]

for ring in rings:
    divisor = gcd(max(ring, first), min(ring, first))
    print("{}/{}".format(first//divisor, ring//divisor))
