def find_five(number):
    result = 0
    divisor = 5
    power = 1
    while number >= divisor:
        result += number // divisor
        power += 1
        divisor *= 5
    return result


n, m = map(int, input().split())

temp_result = find_five(n) - find_five(m) - find_five(n-m)
count_two = 0

temp = m
while temp > 0:
    count_two -= temp // 2
    temp = temp // 2


temp = n - m
while temp > 0:
    count_two -= temp // 2
    temp = temp // 2

temp = n
while temp > 0:
    count_two += temp // 2
    temp = temp // 2
    if count_two >= temp_result:
        break

if count_two <= 0:
    print(0)
elif count_two < temp_result:
    print(count_two)
else:
    print(temp_result)
