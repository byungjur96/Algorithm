n = int(input())
left = 0

for _ in range(n):
    student, apple = map(int, input().split())
    left += (apple % student)

print(left)
