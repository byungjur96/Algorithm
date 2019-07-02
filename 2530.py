hour, minute, second = map(int, input().split(' '))
time = int(input())
second += time
minute += int(second/60)
second = second % 60
hour += int(minute/60)
hour = hour % 24
minute = minute % 60

print(str(hour) + ' ' + str(minute) + ' ' + str(second))
