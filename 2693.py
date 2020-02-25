case = int(input())
for _ in range(case):
    a = list(map(int, input().split()))
    top = []
    for num in a:
        if len(top) == 0:
            top.append(num)
        elif len(top) < 3:
            if top[len(top)-1] < num:
                top.append(num)
            else:
                for i in range(len(top)):
                    if top[i] > num:
                        top.insert(i, num)
                        break
        else:
            if top[2] < num:
                top.append(num)
                top = top[1:]
            for i in range(len(top)):
                if top[i] > num:
                    top.insert(i, num)
                    top = top[1:]
                    break
    print(top[0])
