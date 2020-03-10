n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
targets = list(map(int, input().split()))


def binary_search(target, start, end):
    if start == end:
        return a[start] == target
    mid = (start+end) // 2
    if a[mid] > target:
        return binary_search(target, start, mid)
    elif a[mid] < target:
        return binary_search(target, mid+1, end)
    else:
        return True


for t in targets:
    if binary_search(t, 0, n-1):
        print("1")
    else:
        print("0")
