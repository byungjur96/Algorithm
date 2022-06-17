n,b = input().split()
b = int(b)
n = list(n)

result = 0
size = 1

while n:
    val = n.pop()
    if '0' <= val <= '9':
        val = int(val)
    else:
        val = 10 + ord(val) - ord('A')
    result += val*size
    size*=b
print(result)