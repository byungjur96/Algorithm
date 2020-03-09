import sys

num = int(input())
stairs = []
val = [[0, 0]]
for _ in range(num):
    stairs.append(int(sys.stdin.readline().rstrip()))
    # 연속으로 올라온 계단 수: [0(2칸 넘어온 경우), 1(0에서 1칸 넘어온 경우)]
    val.append([0 for _ in range(2)])

val[1] = [0, stairs[0]]
if num > 1:
    val[2] = [stairs[1], stairs[0] + stairs[1]]

for i in range(3, num+1):
    val[i][0] = max(val[i-2]) + stairs[i-1]
    val[i][1] = val[i-1][0] + stairs[i-1]

print(max(val[num]))
