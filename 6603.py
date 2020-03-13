import sys


def selected_k(array, pos):
    if len(array) == 6:
        val = map(str, array)
        print(" ".join(val))
        return
    if pos == k:
        return

    selected_k(array+[line[pos]], pos+1)
    selected_k(array, pos + 1)


while True:
    # Test Case 정리
    line = sys.stdin.readline().rstrip()
    if line == "0":
        sys.exit()
    line = list(map(int, line.split()))
    k = line[0]
    line = line[1:]
    selected_k([], 0)
    print()
