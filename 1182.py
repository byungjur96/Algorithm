n, s = map(int, input().split())
nums = list(map(int, input().split()))
result = 0
subsums = []
count = 0

for i in range(n):
    for k in range(count):
        subsums.append(subsums[k]+nums[i])
        if subsums[k]+nums[i] == s:
            result += 1
    subsums.append(nums[i])
    count = count * 2 + 1
    if nums[i] == s:
        result += 1

print(result)
