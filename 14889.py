import sys


def cal_team(arr1, arr2):
    mem = n // 2
    val = 0
    for i in range(mem - 1):
        for j in range(i+1, mem):
            val += ability[arr1[i]][arr1[j]]
            val += ability[arr1[j]][arr1[i]]
            val -= ability[arr2[i]][arr2[j]]
            val -= ability[arr2[j]][arr2[i]]
    return abs(val)


def divide_team(arr1, arr2, pos):
    global smallest
    if pos == n:
        smallest = min(smallest, cal_team(arr1, arr2))
    if len(arr1) < n // 2:
        divide_team(arr1 + [pos], arr2, pos + 1)
    if len(arr2) < n // 2:
        divide_team(arr1, arr2 + [pos], pos + 1)


n = int(input())
ability = []
total = 0
smallest = 50 * n

for _ in range(n):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    ability.append(line)
    total += sum(line)

divide_team([], [], 0)
print(smallest)
