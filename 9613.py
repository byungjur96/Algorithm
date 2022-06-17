import sys

def gcd(a, b):
    a, b = min(a,b), max(a,b)
    while a>0:
        a, b = b%a, a
    return b

t = int(sys.stdin.readline())
cases = []

for _ in range(t):
    cases.append(list(map(int, sys.stdin.readline().split())))

for case in cases:
    result = 0
    n = case[0]
    nums = case[1:]
    for i in range(n-1):
        for j in range(i+1, n):
            result += gcd(nums[i], nums[j])
    print(result)
