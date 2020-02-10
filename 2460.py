total = 0
max_val = 0

for i in range(10):
    a, b = input().split()
    a = int(a)
    b = int(b)
    total -= a
    total += b
    if total > 10000:
        total = 10000
    if total > max_val:
        max_val = total
print(max_val)
