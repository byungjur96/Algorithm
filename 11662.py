from math import sqrt

ax, ay, bx, by, cx, cy, dx, dy = map(int, input().split())

def calculate_distance(t):
    minho_x = (bx - ax) * t + ax
    gangho_x = (dx - cx) * t + cx

    minho_y = (by - ay) * t + ay
    gangho_y = (dy - cy) * t + cy

    dis = (minho_x - gangho_x) ** 2 + (minho_y - gangho_y) ** 2
    return dis

eps = 1e-7
hi = 1
lo = 0
while abs(hi-lo) > eps:
    m1 = lo + (hi - lo)/3
    m2 = hi - (hi - lo)/3
    fm1 = calculate_distance(m1)
    fm2 = calculate_distance(m2)
    if fm1 > fm2:
        lo = m1
    elif fm1 < fm2:
        hi = m2
    else:
        lo = m1
        hi = m2

print(sqrt(calculate_distance(lo)))