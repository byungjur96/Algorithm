n, k = map(int, input().split())

p = [i+1 for i in range(n)]
result = []
counter = 0
while p:
    counter = (counter+k-1) % len(p)
    result.append(p.pop(counter))

print("<"+", ".join(list(map(str,result)))+">")