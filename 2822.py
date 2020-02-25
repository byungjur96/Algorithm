score = []

questions = []
final = 0

for i in range(8):
    score.append((i+1, int(input())))

score.sort(key=lambda a: a[1])
for i in range(3,8):
    questions.append(str(score[i][0]))
    final += score[i][1]
questions.sort()

print(final)
print(" ".join(questions))
