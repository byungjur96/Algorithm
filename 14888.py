import sys
orig_sign = ["+", "-", "*", "%"]

n = int(input())  # 수의 개수
sequences = list(map(int, input().split()))  # 숫자들의 순서
each_sign = list(map(int, input().split()))  # 각 연산자의 개수

max_val = -(10**9)
min_val = 10**9


# orders: 결정된 연산자의 순서
# left_signs: 각 연산자들의 남은 개수
def calculation(left_signs, orders):
    global max_val, min_val
    # 남은 연산자의 개수가 0개면 비교한다.
    if sum(left_signs) == 0:
        temp = sequences[0]
        for i in range(sum(each_sign)):
            if orders[i] == "+":
                temp += sequences[i+1]
            elif orders[i] == "-":
                temp -= sequences[i + 1]
            elif orders[i] == "*":
                temp *= sequences[i+1]
            elif orders[i] == "%":
                if temp < 0:
                    temp *= -1
                    temp = temp // sequences[i+1]
                    temp *= -1
                else:
                    temp = temp // sequences[i + 1]

        max_val = max(temp, max_val)
        min_val = min(temp, min_val)
        return

    [plus, minus, multi, divide] = left_signs
    if plus > 0:
        calculation([plus-1, minus, multi, divide], orders+["+"])
    if minus > 0:
        calculation([plus, minus-1, multi, divide], orders+["-"])
    if multi > 0:
        calculation([plus, minus, multi-1, divide], orders+["*"])
    if divide > 0:
        calculation([plus, minus, multi, divide-1], orders+["%"])


calculation(each_sign, [])

print(max_val)
print(min_val)