n = int(input())

def make_star(star, blank):
    l = len(star)
    result = []
    for i in range(l):
        result.append(star[i % l] * 3)
    for i in range(l, 2*l):
        result.append(star[i % l] + blank[i % l] + star[i % l])
    for i in range(2*l, 3*l):
        result.append(star[i % l] * 3)
    return result

def make_blank(blank):
    result = []
    for i in range(3*len(blank)):
        result.append(blank[i % len(blank)] * 3)
    return result

star = ['*']
blank = [' ']

while n > 1:
    star, blank = make_star(star, blank), make_blank(blank)
    n = n // 3
for s in star:
    print(s)