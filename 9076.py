case = int(input())
for _ in range(case):
    score = list(map(int, input().split()))
    score.sort()
    score = score[1:4]
    if score[2] - score[0] < 4:
        print(sum(score))
    else:
        print("KIN")
