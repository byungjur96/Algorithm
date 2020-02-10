exist = [False for _ in range(42)]
count = 0

for _ in range(10):
    val = int(input()) % 42
    if exist[val] is False:
        exist[val] = True
        count += 1

print(count)
