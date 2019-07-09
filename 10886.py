n = int(input())
val = 0
for _ in range(n):
    temp = int(input())
    if temp == 0:
        val -= 1
    else:
        val += 1

if val > 0:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
