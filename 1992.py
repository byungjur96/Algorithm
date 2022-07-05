import sys

def check(lst):
    v = lst[0][0]
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][j] != v:
                return False
    return True

def zip(lst):
    if check(lst):
        return str(lst[0][0])
    else:
        result = "("
        l = len(lst)
        for j in range(2):
            for i in range(2):
                result += zip([lst[a][i*(l//2):(i+1)*(l//2)] for a in range(j*(l//2), (j+1)*(l//2))])
        return result + ")"

img = []
n = int(sys.stdin.readline())
for _ in range(n):
    img.append(list(map(int, list(sys.stdin.readline().rstrip()))))

print(zip(img))