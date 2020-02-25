case = int(input())

for _ in range(case):
    line = input()
    if ord('a') <= ord(line[0]) <= ord('z'):
        print(chr(ord(line[0]) + ord('A') - ord('a')) + line[1:])
    else:
        print(line)
