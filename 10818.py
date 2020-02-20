num = int(input())
num_list = list(map(int, input().split()))

min_val = num_list[0]
max_val = num_list[0]

for i in num_list:
    if i < min_val:
        min_val = i
    if i > max_val:
        max_val = i

print(min_val, end=" ")
print(max_val)
