import sys

num = int(input())
meetings = []
total = 0
end_time = 0  # 회의 막 끝난 시

for _ in range(num):
    meetings.append(list(map(int, input().split())))

# meetings.sort(key=lambda m: m[0])
# meetings.sort(key=lambda m: m[1])
meetings.sort(key=lambda m: [m[1], m[0]])
for [start, end] in meetings:
    if start >= end_time:
        end_time = end
        total += 1

print(total)
