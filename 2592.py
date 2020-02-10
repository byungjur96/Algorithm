# 값들의 종류
lst = []
# input 값 10번에 대한 for 문
for i in range(10):
    val = int(input())
    check = False

    for j in range(len(lst)):
        # 이미 존재하는 값이면 cnt를 늘려준다.
        if lst[j][0] == val:
            lst[j][1] += 1
            check = True
    # 존재하지 않는 값이면 새로 추가해준다.
    if check is False:
        lst.append([val, 1])

# 최빈값 확인
max_val = 0
total_val = 0
for i in range(len(lst)):
    total_val += (lst[i][0]*lst[i][1])
    if lst[i][1] > lst[max_val][1]:
        max_val = i

print(int(total_val/10))
print(lst[max_val][0])
