m, n = map(int, input().split())

a = [True] * (n+1)
a[0] = False
a[1] = False
for i in range(2, n+1):
    if a[i] == False:
        continue
    mul = 2
    while i*mul <= n:
        a[i*mul] = False
        mul+=1

result = []
for i in range(m, n+1):
    if a[i]:
        result.append(i)
for r in result: print(r)