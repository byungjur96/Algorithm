n, k = input().split(" ")
an = list(map(int, input().split(" ")))
an.sort()
print(an[int(k)-1])
