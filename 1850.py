a, b = map(int, input().split())
a, b = min(a, b), max(a ,b)

while a > 0:
    a, b = b%a, a

print("1"*b)