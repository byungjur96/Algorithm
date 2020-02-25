line = input()
count = 1

for l in line:
    if l == ',':
        count += 1

print(count)
