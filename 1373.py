a = list(input())
result = ""
temp = 0
count = 0
while a:
    val = int(a.pop())
    temp += val*(2**count)
    count += 1
    if count%3==0:
        result = str(temp) + result
        temp = 0
        count = 0
if result == "" or temp != 0:
    result = str(temp) + result
print(result)