current_time = list(map(int, input().split(':')))
end_time = list(map(int, input().split(':')))

current_sec = current_time[0]*3600 + current_time[1]*60 + current_time[2]
end_sec = end_time[0]*3600 + end_time[1]*60 + end_time[2]

if end_sec < current_sec:
    end_sec += 24*3600

left_time = end_sec - current_sec
left_sec = left_time % 60

left_min = int(left_time/60)
if left_min < 60:
    left_hour = 0
else:
    left_hour = left_min // 60
    left_min %= 60

print("{0:02}:{1:02}:{2:02}".format(left_hour, left_min, left_sec))
