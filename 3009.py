x_val = dict()
y_val = dict()

for _ in range(3):
    x, y = input().split()
    if x in x_val.keys():
        x_val[x] += 1
    else:
        x_val[x] = 1
    if y in y_val.keys():
        y_val[y] += 1
    else:
        y_val[y] = 1

for temp_x in x_val:
    if x_val[temp_x] == 1:
        missing_x = temp_x
for temp_y in y_val:
    if y_val[temp_y] == 1:
        missing_y = temp_y

print(missing_x, missing_y)
