import sys

n = int(input())
people = []
ranks = []

for _ in range(n):
    people.append(list(map(int, sys.stdin.readline().rstrip().split())))

for person in people:
    rank = 1
    for others in people:
        if person[0] < others[0] and person[1] < others[1]:
            rank += 1
    ranks.append(str(rank))

print(" ".join(ranks))
