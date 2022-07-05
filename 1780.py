import sys

result = {-1:0, 0:0, 1:0}

def check_paper(lst):
    v = lst[0][0]
    size = len(lst)
    if size == 1:
        result[v] += 1
        return
    for i in range(size):
        for j in range(size):
            if lst[i][j] != v:
                size = size // 3
                for x in range(3):
                    for y in range(3):
                        check_paper([lst[a][size*y:size*(y+1)] for a in range(size*x, size*(x+1))])
                return
    result[v] += 1
    return

n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
check_paper(paper)
print(result[-1])
print(result[0])
print(result[1])