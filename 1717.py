import sys


def get_parent(x):
    if mother[x] == x:
        return x
    return get_parent(mother[x])


n, m = map(int, input().split())
mother = [i for i in range(n+1)]

for _ in range(m):
    cal, a, b = map(int, sys.stdin.readline().rstrip().split())
    # 합친다.
    if cal == 0:
        mother_a = get_parent(a)
        mother_b = get_parent(b)
        mother[max(mother_a, mother_b)] = min(mother_a, mother_b)
    # 확인한다.
    else:
        if get_parent(a) == get_parent(b):
            print("YES")
        else:
            print("NO")
