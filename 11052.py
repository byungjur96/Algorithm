n = int(input())
p = list(map(int, input().split()))

lst = [p[0]]

for i in range(1, n):
    temp = p[i]
    for j in range(i):
        if temp < lst[j] + p[i-j-1]:
            temp = lst[j] + p[i-j-1]
    lst.append(temp)

print(lst[n-1])