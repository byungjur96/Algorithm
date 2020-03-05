n = int(input())
cards = [(i+1) for i in range(n)]
start = 0

while n > 1:
    start += 1
    cards.append(cards[start])
    start += 1
    n -= 1

print(cards[-1])
