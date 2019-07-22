semester = int(input())
for _ in range(semester):
    section = int(input())
    total_c = 0
    total_g = 0
    for _ in range(section):
        c, g = input().split()
        c = int(c)
        g = float(g)
        total_c += c
        total_g += (c*g)
    print(total_c, round(total_g/total_c, 1))
