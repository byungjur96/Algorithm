def solve(left, right):
    if left == right:
        return h[left]
    mid = int((left+right)/2)
    ret = max(solve(left, mid), solve(mid+1, right))
    lo = mid
    hi = mid + 1
    height = min(h[lo], h[hi])
    ret = max(ret, height * 2)
    while left < lo or hi < right:
        if hi < right and(lo == left or h[lo-1] < h[hi+1]):
            hi += 1
            height = min(height, h[hi])
        else:
            lo -= 1
            height = min(height, h[lo])

        ret = max(ret, height*(hi - lo + 1))
    return ret


case = int(input())
for _ in range(case):
    length = int(input())
    h = list(map(int, input().split()))
    print(solve(0, length-1))

