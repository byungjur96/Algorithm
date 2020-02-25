case = int(input())
for i in range(case):
    score = list(map(int, input().split()))
    print("Class {}".format(i+1))
    students = score[0]
    score = score[1:]
    score.sort()
    max_gap = 0
    for j in range(students - 1):
        val = abs(score[j+1] - score[j])
        if val > max_gap:
            max_gap = val
    print("Max {}, Min {}, Largest gap {}".format(score[students-1], score[0], max_gap))
