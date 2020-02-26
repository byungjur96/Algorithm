import math

start, end = map(int, input().split())
total = 0

val = 1
while int(val*(val-1)/2+1) < start:
    val += 1

val -= 1

while start <= end:
    if int(val * (val + 1) / 2 + 1) == start:
        val += 1
    total += val
    start += 1

print(total)
