coins = [500, 100, 50, 10, 5, 1]

change = 1000 - int(input())
result = 0

for coin in coins:
    while coin <= change:
        change -= coin
        result += 1

print(result)
