import sys

def check_existance(lst, k):
    high = len(lst)
    low = -1
    while low + 1 < high:
        mid = (high + low) // 2
        if lst[mid] > k:
            high = mid
        elif lst[mid] < k:
            low = mid
        else:
            return "1"
    return "0"

m = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()
m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))
result = []
for target in targets:
    result.append(check_existance(cards, target))
print(" ".join(result))