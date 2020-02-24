num = list(map(int, input().split()))

if num[1] < num[0]:
    temp = num[1]
    num[1] = num[0]
    num[0] = temp

if num[2] < num[1]:
    if num[2] > num[0]:
        temp = num[2]
        num[2] = num[1]
        num[1] = temp
    else:
        temp = num[0]
        num[0] = num[2]
        num[2] = num[1]
        num[1] = temp

print(" ".join(list(map(str, num))))