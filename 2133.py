n = int(input())

lst = [[0, 1, 0, 1, 0, 0, 0, 1], [3, 0, 0, 0, 1, 0, 1, 0]]

for i in range(2, n):
    temp = [lst[i-1][1]+lst[i-1][3]+lst[i-1][7], lst[i-1][0]+lst[i-1][6], lst[i-1][5], lst[i-1][0]+lst[i-1][4], lst[i-1][3], lst[i-1][2], lst[i-1][1], lst[i-1][0]]
    lst.append(temp)

print(lst[n-1][0])