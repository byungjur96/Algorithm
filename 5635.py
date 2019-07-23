n = int(input())
oldest = None
youngest = None

for _ in range(n):
    name, d, m, y = input().split()
    d = d.zfill(2)
    m = m.zfill(2)
    y = y.zfill(2)
    full_date = int(y + m + d)
    if oldest is None or oldest[1] > full_date:
        oldest = [name, full_date]
    if youngest is None or youngest[1] < full_date:
        youngest = [name, full_date]

print(youngest[0])
print(oldest[0])
