def count_pairings():

    first_person = -1
    for j in range(n):
        if taken[j] is False:
            first_person = j
            break

    # 모든 사람한테 배정이 끝나면 return
    if first_person == -1:
        return 1
    result = 0

    for k in range(first_person+1, n):
        if isFriend[first_person][k] is True and taken[k] is False:
            taken[first_person] = True
            taken[k] = True
            result += count_pairings()
            taken[first_person] = False
            taken[k] = False

    return result


test_case = int(input())
for _ in range(test_case):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    taken = [False for _ in range(n)]
    isFriend = [[False for _ in range(n)] for _ in range(n)]
    # 친구 관계 표시
    for i in range(m):
        if arr[2 * i] > arr[2 * i + 1]:
            isFriend[arr[2 * i + 1]][arr[2 * i]] = True
        else:
            isFriend[arr[2 * i]][arr[2 * i + 1]] = True
    print(count_pairings())
