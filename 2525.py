hour, minute = map(int, input().split(" "))
takes = int(input())
minute += takes
print(str((hour+int(minute/60)) % 24) + " " + str((minute) % 60))
