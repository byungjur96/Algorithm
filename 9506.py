while True:
    n = int(input())
    div = []
    sum = 0
    if n == -1:
        exit()
    for i in range(1, n):
        if n % i == 0:
            div.append(i)
            sum += i
    if sum == n:
        print(n, end=" = ")
        for i in range(len(div)-1):
            print(div[i], end=" + ")
        print(div[-1])
    else:
        print(n, end=" is NOT perfect.\n")
