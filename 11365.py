import sys

while True:
    line = input()
    if line == 'END':
        sys.exit()
    else:
        for i in range(len(line)-1, -1, -1):
            print(line[i], end="")
        print()
