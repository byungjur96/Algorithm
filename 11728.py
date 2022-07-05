n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
result = []

a_idx = 0
b_idx = 0

while a_idx < n or b_idx < m:
    if a_idx == n:
        result.append(b[b_idx])
        b_idx += 1
    elif b_idx == m:
        result.append(a[a_idx])
        a_idx += 1
    elif a[a_idx] < b[b_idx]:
        result.append(a[a_idx])
        a_idx += 1
    elif b[b_idx] <= a[a_idx]:
        result.append(b[b_idx])
        b_idx += 1

print(" ".join(list(map(str, result))))