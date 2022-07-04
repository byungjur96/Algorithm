import sys
from bisect import bisect_left, bisect_right

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))
cards.sort()

result = [max(0, bisect_right(cards, target) - bisect_left(cards, target)) for target in targets]
print(" ".join(list(map(str, result))))