n, k = map(int, input().split())

lst = [[1] * (n+1)]

for i in range(k-1):
    temp = []
    for x in range(n+1):
        temp.append(sum(lst[i][:x+1]))
    lst.append(temp)

print(lst[k-1][n] % 1000000000)