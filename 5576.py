score = []

for _ in range(20):
    score.append(int(input()))

w_univ = score[:10]
k_univ = score[10:]

w_univ.sort()
k_univ.sort()

print(w_univ)
print(k_univ)

print("{} {}".format(sum(w_univ[7:]), sum(k_univ[7:])))
