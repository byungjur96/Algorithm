import sys

fibonacci = [[1, 0], [0, 1]]

case = int(input())

for _ in range(case):
    val = int(sys.stdin.readline().rstrip())
    if val < len(fibonacci):
        print("{} {}".format(fibonacci[val][0], fibonacci[val][1]))
    else:
        for i in range(len(fibonacci), val+1):
            zero = (fibonacci[i - 1][0] + fibonacci[i - 2][0])
            one = fibonacci[i - 1][1] + fibonacci[i - 2][1]
            fibonacci.append([zero, one])
        print("{} {}".format(fibonacci[val][0], fibonacci[val][1]))
