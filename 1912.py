num = int(input())
array = list(map(int, input().split()))
total_sum = [array[0]]


min_val = 0
gap = max(array)

# total_sum[i]: array[i]까지의 sum
for i in range(1, num):
    # val: i까지 전체 합
    val = total_sum[i-1]+array[i]
    total_sum.append(val)
    # 만약 값이 감소했다면 바닥 값을 바꾼다.
    if val < min_val:
        min_val = val
    # 만약 값이 증가했다면 바닥으로부터의 거리를 비교한다.
    else:
        gap = max(gap, val - min_val)
print(gap)
