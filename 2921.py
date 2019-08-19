n = int(input())
dots = 0
for i in range(n+1):
    dots += int(i*(i+1)*3/2)
print(dots)
