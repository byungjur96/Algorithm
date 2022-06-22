def cal(n, p):
    result = 0
    lst = list(map(int,list(str(n))))
    for l in lst:
        result += power[l]
    return result

a, p = map(int, input().split())
exist = []
power = [i**p for i in range(10)]
val = a

while val not in exist:
    exist.append(val)
    val = cal(val, p)

print(exist.index(val))
