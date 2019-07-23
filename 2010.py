import sys

n = int(input())
total = -n

for _ in range(n):
    temp_count = int(sys.stdin.readline().rstrip())
    total += temp_count

print(total+1)
