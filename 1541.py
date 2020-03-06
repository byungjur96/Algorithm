exp = input()
result = 0

# 뺄셈 기준으로 나눠준다.
subtractions = exp.split("-")

for sub in range(len(subtractions)):
    addition = list(map(int, subtractions[sub].split("+")))
    temp = sum(addition)
    if sub == 0:
        result += temp
    else:
        result -= temp

print(result)
