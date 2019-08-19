count = 0
day = input()
cars = input().split()
for car in cars:
    if car == day:
        count += 1
print(count)
