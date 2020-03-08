import sys

n = int(input())

exist = False
for i in range(1, n+1):
    val = i
    str_val = str(i)
    for s in str_val:
        val += int(s)
    if val == n:
        exist = True
        print(i)
        sys.exit()

print(0)
