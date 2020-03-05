n, k = map(int, input().split())

people = [(i+1) for i in range(n)]
result = []

pos = -1


for i in range(n):
    count = 0
    while count != k:
        pos += 1
        if people[pos % n] is not None:
            count += 1
    result.append(str(people[pos % n]))
    people[pos % n] = None
print("<" + ", ".join(result) + ">")

