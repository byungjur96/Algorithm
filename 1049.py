n, m = map(int, input().split())
six = 1000
one = 1000
for i in range(m):
    package, each = map(int, input().split())
    six = min(package, six)
    one = min(one, each)

# 패키지보다 단일 6개가 더 저렴할 때.
if six > one * 6:
    print(one*n)
# 패키지 사고 남은 거 단일보다 패키지가 더 저렴할 떄.
elif six < one * (n % 6):
    print(six * (n // 6 + 1))
# 패키지 사고 남은 거는 단일로 살 때.
else:
    print(six*(n // 6) + one * (n % 6))
