max_val = 0
idx = -1
for i in range(9):
    val = int(input())
    if val > max_val:
        max_val = val
        idx = i + 1
print(max_val)
print(idx)
