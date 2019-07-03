def is_palindrome():
    line = input()
    n = len(line)
    for i in range(int(n/2)):
        if line[i] != line[n-1-i]:
            return False
    return True


if is_palindrome():
    print(1)
else:
    print(0)
