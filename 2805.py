import sys

def check(lst, k):
    result = 0
    for l in lst:
        if l > k:
            result += (l - k)
    return result

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
low = 0
high = max(trees) + 1
while low + 1 < high:
    mid = (low + high) // 2
    temp = check(trees, mid)
    if temp >= m:
        low = mid
    else:
        high = mid

print(low)

