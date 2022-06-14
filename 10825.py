import sys

n = int(sys.stdin.readline())
students = []
score = []

for _ in range(n):
    students.append(sys.stdin.readline())

for student in students:
    temp = 0
    info = student.split()
    temp += (int(info[3]) - 1) + 100 * (100 - int(info[2])) + 10000 * (int(info[1]) - 1)
    name = info[0]
    idx = 100
    for n in name:
        temp += (ord('z') - ord(n))/idx
        idx *= 100
    score.append([info[0], temp])

score.sort(key=lambda x: x[1], reverse=True)

for s in score:
    print(s[0])