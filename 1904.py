result = [1, 2]

n = int(input())

for i in range(2, n):
    val = (result[i-2] + result[i-1]) % 15746
    result.append(val)

print(result[n - 1])
