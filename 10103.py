point = [100, 100]
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    if a < b:
        point[0] -= b
    elif b < a:
        point[1] -= a

print(point[0])
print(point[1])
