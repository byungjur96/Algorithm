def dec(s):
    l = len(s)
    count = [0] * l
    
    if l == 1:
        if int(s) > 0:
            return 1
        else:
            return 0
    if s[0] == '0':
        return 0

    if int(s[0]) > 0:
        count[0] = 1
    
    if int(s[1]) > 0:
        count[1] += 1

    if 9 < int(s[0] + s[1]) <= 26:
        count[1] += count[0]

    for i in range(2, l):
        if s[i] != '0':
            count[i] = count[i-1]
        if 9 < int(s[i-1] + s[i]) <= 26:
            count[i] += count[i-2]
    # print(count)
    return count[l-1]
    
print(dec(input()) % 1000000)