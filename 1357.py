def rev(num):
    string = str(num)
    new_val = ""
    for i in range(len(string)-1, -1, -1):
        new_val += string[i]
    return int(new_val)


a, b = map(int, input().split())
print(rev(rev(a) + rev(b)))
