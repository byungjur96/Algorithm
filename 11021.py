num = int(input())
result = []

for _ in range(num):
    a, b = input().split(" ")
    result.append(int(a) + int(b))

for i in range(num):
    print('Case #' + str(i+1) + ': ' + str(result[i]))
