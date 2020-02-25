case = int(input())

for _ in range(case):
    first, second = input().split()
    length = len(first)
    dis = []
    for l in range(length):
        if ord(second[l]) > ord(first[l]):
            dis.append(str(ord(second[l]) - ord(first[l])))
        elif ord(second[l]) < ord(first[l]):
            dis.append(str(26 + ord(second[l]) - ord(first[l])))
        else:
            dis.append("0")
    print("Distances:" + " ".join(dis))
