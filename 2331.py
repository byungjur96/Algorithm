def cal(n, p):
    result = 0
    lst = list(map(int,list(str(n))))
    for l in lst:
        result += (l**p)
    return result

a, p = map(int, input().split())

exist = []

val = a

while val not in exist:
    exist.append(val)
    val = cal(val, p)

print(exist.index(val))
