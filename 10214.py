t = int(input())

for _ in range(t):
    score = 0
    for _ in range(9):
        y, k = map(int, input().split())
        score = score + k - y
    if score > 0:
        print("Korea")
    elif score < 0:
        print("Yonsei")
    else:
        print("Draw")
