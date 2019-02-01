t = int(input())

for _ in range(t):
    n = int(input())
    case = [1, 1, 2] # 0, 1, 2
    for i in range(3, n+1):
        case.append(case[i-1]+case[i-2]+case[i-3])
    print(case[n])
