n, m = map(int, input().split())
cards = list(map(int, input().split()))

maximum = -1

for x in range(n-2):
    for y in range(x+1, n-1):
        for z in range(y+1, n):
            val = cards[x] + cards[y] + cards[z]
            if m >= val > maximum:
                maximum = val

print(maximum)
