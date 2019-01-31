edge = int(input())
vertex = []
a = 0
b = 0

for _ in range(edge):
    x, y = input().split(" ")
    vertex.append([int(x), int(y)])

for i in range(edge - 1):
    a += vertex[i][0] * vertex[i+1][1]
    b += vertex[i][1] * vertex[i+1][0]
a += vertex[edge-1][0] * vertex[0][1]
b += vertex[0][0] * vertex[edge-1][1]

area = abs(a - b)/2

print(round(area, 2))
