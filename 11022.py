num = int(input())
result = []

for _ in range(num):
    a, b = input().split(" ")
    result.append([a, b])

for i in range(num):
    print('Case #' + str(i+1) + ': ' + result[i][0] + ' + ' + result[i][1] + " = " + str(int(result[i][0])+int(result[i][1])))
