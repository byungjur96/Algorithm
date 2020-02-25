nums = []
total = -100

for i in range(9):
    val = int(input())
    nums.append(val)
    total += val
found = False
for i in range(8):
    if found:
        break
    for j in range(i, 9):
        if found:
            break
        if nums[i] + nums[j] == total:
            del nums[j]
            del nums[i]
            found = True
for i in nums:
    print(i)
