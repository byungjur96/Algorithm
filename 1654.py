import sys

def check(arr, l):
    result = 0
    for a in arr:
        result += (a // l)
    return result

k, n = map(int, sys.stdin.readline().split())
lan = []
for _ in range(k):
    lan.append(int(sys.stdin.readline()))

low = 1
high = max(lan) + 1
mid = high // 2
while low + 1 < high:
    if check(lan, mid) >= n:
        low = mid
    elif check(lan, mid) < n:
        high = mid
    mid = (high + low) // 2
    
print(low)