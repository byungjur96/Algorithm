case = int(input())

for _ in range(case):
    pointer, word = input().split()
    pointer = int(pointer)
    print(word[:pointer-1], end="")
    print(word[pointer:])
