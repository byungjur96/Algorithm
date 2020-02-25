# # 가장 단순한 풀이
def sol1():
    nums = []
    total = 0

    for _ in range(5):
        num = int(input())
        nums.append(num)
        total += num

    nums.sort()

    print(int(total/5))
    print(nums[2])


# 정통 풀이
def sol2():
    nums = []
    total = 0

    for i in range(5):
        num = int(input())
        total += num
        pos = 0
        for j in range(i):
            if num > nums[j]:
                pos = j + 1
        if pos == i:
            nums.append(num)
        else:
            nums.insert(pos, num)

    print(int(total/5))
    print(nums[2])
