import sys

height = []
total = 0
for _ in range(9):
    val = int(input())
    height.append(val)
    total += val

total -= 100

for i in range(8):
    for j in range(i+1, 9):
        if height[i] + height[j] == total:
            del height[j]
            del height[i]
            height.sort()
            for h in height:
                print(h)
            sys.exit()
