n = int(input())
count = [[0 for _ in range(10)] for _ in range(n)]

count[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, n):
    for j in range(10):
        if j == 0:
            count[i][j] = count[i - 1][j + 1]
        elif j == 9:
            count[i][j] = count[i - 1][j - 1]
        else:
            count[i][j] = count[i - 1][j - 1] + count[i - 1][j + 1]

print(sum(count[n-1]) % 1000000000)
