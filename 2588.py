value = []
sum_value = 0
a = int(input())
b = input()
for i in range(3):
    value.append(a*int(b[2-i]))

for i in range(3):
    print(value[i])
    sum_value += value[i]*(10**i)
print(sum_value)
