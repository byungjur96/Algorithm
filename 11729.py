n = int(input())

def hanoi(num, start, end):
    if num == 1:
        print(start, end)
        return
    hanoi(num-1,start, 6-start-end)
    print(start, end)
    hanoi(num-1,6-start-end, end)

print(2**n-1)
hanoi(n, 1, 3)