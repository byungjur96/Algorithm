a = [True] * 1001
a[0] = False
a[1] = False
for i in range(2, 1001):
    if a[i] == False:
        continue
    mul = 2
    while i*mul <= 1000:
        a[i*mul] = False
        mul+=1

n = int(input())
lst = list(map(int, input().split()))

count = 0
for l in lst:
    if a[l]:
        count+=1

print(count)