t = int(input())

for _ in range(t):
    n = int(input())
    point = [list(map(int, input().split())) for _ in range(2)]

    a, b, c, d = 0, point[0][0], 0, point[1][0]
    
    for i in range(1, n):
        a, b, c, d = b, max(a, c, d)+point[0][i], d, max(a,b,c)+point[1][i]
    print(max(a,b,c,d))