import sys

max_val = 1000000

a = [True] * (max_val+1)
a[0] = False
a[1] = False
target = []

for i in range(2, max_val+1):
    if a[i] == False:
        continue
    target.append(i)
    mul = 2
    while i*mul <= max_val:
        a[i*mul] = False
        mul+=1
target.pop(0)

def goldbach():
    while True:
        n = int(sys.stdin.readline())
        if n == 0:
            return
        for t in target:
            if 2*t > n:
                print("Goldbach's conjecture is wrong.")
                break
            if a[n-t]:
                print('{} = {} + {}'.format(n, t, n-t))
                break

goldbach()