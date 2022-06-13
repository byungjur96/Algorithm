n = int(input())

lst = [i for i in range(n+1)]
idx = 1
for i in range(1, n+1):
    if i == idx**2:
        lst[i] = 1
        idx+=1
    else:
        for j in range(1, idx):
            lst[i] = min(lst[i], lst[i-(j**2)]+1)
print(lst[n])