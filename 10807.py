num = int(input())
val = list(map(int, input().split()))
target = int(input())

count = 0

for i in val:
    if i == target:
        count += 1

print(count)
