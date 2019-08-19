test = int(input())

for i in range(test):
    a, b = map(int, input().split())
    print("Case {0}: {1}".format(i+1, a+b))
