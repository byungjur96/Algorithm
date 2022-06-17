def convert(n):
    if n<10:
        return str(n)
    else:
        return chr(ord('A') + n - 10)

n, b = map(int, input().split())
result = ""

while n > 0:
    val = n % b
    result = convert(val) + result
    n = (n-val)//b

print(result)