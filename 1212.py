m = ['000', '001', '010', '011', '100', '101', '110', '111']
n = list(map(int, list(input())))
converted = []
result = ""
idx = len(n)-1
while idx >= 0:
    val = n[idx]
    idx-=1
    converted.append(m[val])
while converted:
    result+=converted.pop()
while result[0] == '0' and len(result)>1:
    result = result[1:]
print(result)