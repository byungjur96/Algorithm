n = int(input())
a = list(map(int, input().split()))

# possible[i]: i가 마지막 원소인 부분순열의 최대 길이
# 가장 짧을 때: 자기자신
possible = [1 for _ in range(n)]

for i in range(n):
    for s in range(i):
        # a[i]가 a[s]보다 크면 possible[i] = max(possible[i], possible[s]+1)
        if a[s] < a[i] and possible[i] <= possible[s]:
            possible[i] = possible[s] + 1

result = 0
for sub in possible:
    if sub > result:
        result = sub

print(result)
