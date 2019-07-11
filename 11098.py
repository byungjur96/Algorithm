test_case = int(input())

for _ in range(test_case):
    p = int(input())
    best_player = ""
    val = 0
    for _ in range(p):
        price, player = input().split()
        if int(price) > val:
            best_player = player
            val = int(price)
    print(best_player)
