val = 0
num = (input().split())
for n in num:
    val += int(n)**2
print(val % 10)
