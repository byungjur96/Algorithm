coin = []
min_coin = 0
n, k = input().split(" ")
k = int(k)
for _ in range(int(n)):
    coin.append(int(input()))

for i in range(len(coin), 0, -1):
    if int(k/coin[i-1]) > 0:
        min_coin += int(k/coin[i-1])
        k %= coin[i-1]

print(min_coin)
